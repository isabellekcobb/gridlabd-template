def get_meters(glm_file_path):
    meters = []
    with open(glm_file_path, 'r') as f:
        inside_meter_block = False
        for line in f:
            line = line.strip()
            if line.startswith("object meter {"):
                inside_meter_block = True
                meter = {}
            elif inside_meter_block:
                if line.startswith("name "):
                    meter_name = line[len("name "):].rstrip(';')
                    meter['name'] = meter_name
                elif line.startswith("service_level "):
                    service_level = line[len("service_level "):].rstrip(';')
                    meter['service_level'] = service_level
                elif line == "}":
                    meters.append(meter)
                    inside_meter_block = False

    return meters

def main():
    glm_file_path = '123.glm'  # Replace this with the path to your .glm file

    meters = get_meters(glm_file_path)

    if meters:
        print("List of meter objects in the .glm file:")
        for meter in meters:
            print(f"Name: {meter['name']}, Service Level: {meter['service_level']}")
    else:
        print("No meter objects found in the .glm file.")

if __name__ == "__main__":
    main()
