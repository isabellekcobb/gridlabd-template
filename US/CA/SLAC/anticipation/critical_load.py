import re

def get_meter_objects(glm_file_path):
    meter_objects = []
    with open(glm_file_path, 'r') as f:
        glm_content = f.read()

        # Use regular expression to find all meter objects with service_level
        meter_pattern = r"object meter {\s*name (\w+);\s*service_level (HIGH|CRITICAL);"
        matches = re.findall(meter_pattern, glm_content, re.MULTILINE)

        for match in matches:
            meter_name, service_level = match
            meter_objects.append((meter_name, service_level))

    return meter_objects

def main():
    glm_file_path = '123.glm'  # Replace this with the path to your .glm file

    meter_objects = get_meter_objects(glm_file_path)

    if meter_objects:
        print("Meter objects with HIGH or CRITICAL service_level:")
        for meter_name, service_level in meter_objects:
            print(f"{meter_name}: {service_level}")
    else:
        print("No meter objects with HIGH or CRITICAL service_level found in the .glm file.")

if __name__ == "__main__":
    main()
