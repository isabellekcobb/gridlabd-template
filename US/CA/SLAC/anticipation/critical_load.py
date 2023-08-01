import re

def get_all_meters(glm_file_path):
    meter_names = []
    with open(glm_file_path, 'r') as f:
        for line in f:
            # Use regular expression to find the 'object meter' lines and extract the meter name
            match = re.match(r"object meter {\s*name (\w+);", line)
            if match:
                meter_name = match.group(1)
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
