import re

def has_critical_service_level(glm_file_path):
    with open(glm_file_path, 'r') as f:
        glm_content = f.read()

        # Use regular expression to find all meter objects with service_level
        meter_pattern = r"object meter {\s*name (\w+);\s*service_level (\w+);"
        matches = re.finditer(meter_pattern, glm_content)

        for match in matches:
            meter_name, service_level = match.groups()
            if service_level == "CRITICAL":
                return True

    return False

def main():
    glm_file_path = '123.glm'  # Replace this with the path to your .glm file

    if has_critical_service_level(glm_file_path):
        print("Meter object with service_level CRITICAL found in the .glm file.")
    else:
        print("No meter object with service_level CRITICAL found in the .glm file.")

if __name__ == "__main__":
    main()
