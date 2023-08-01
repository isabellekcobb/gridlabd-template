import re

def get_all_meters(glm_file_path):
    meter_names = []
    with open(glm_file_path, 'r') as f:
        glm_content = f.read()

        # Use regular expression to find all meter objects
        meter_pattern = r"object meter {\s*name (\w+);"
        matches = re.findall(meter_pattern, glm_content)

        for match in matches:
            meter_name = match
            meter_names.append(meter_name)

    return meter_names

def main():
    glm_file_path = '123.glm'  # Replace this with the path to your .glm file

    all_meters = get_all_meters(glm_file_path)

    if all_meters:
        print("List of all meters in the .glm file:")
        for meter_name in all_meters:
            print(meter_name)
    else:
        print("No meter objects found in the .glm file.")

if __name__ == "__main__":
    main()
