def extract_meters(input_file_path, output_file_path):
    critical_high_meters = []

    with open(input_file_path, 'r') as input_file:
        current_object = None
        is_inside_meter = False

        for line in input_file:
            if line.strip().lower().startswith("object meter"):
                is_inside_meter = True
                current_object = {"object": "meter"}

            if is_inside_meter:
                parts = line.split('=')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()

                    if key == "service_level" and value in ["CRITICAL", "HIGH"]:
                        current_object[key] = value

                    if key == "name":
                        current_object[key] = value
                        is_inside_meter = False
                        critical_high_meters.append(current_object)

    with open(output_file_path, 'w') as output_file:
        for meter in critical_high_meters:
            output_file.write("object meter;\n")
            for key, value in meter.items():
                output_file.write(f"  {key} = {value};\n")
            output_file.write("\n")

if __name__ == "__main__":
    input_file_path = "123.glm"
    output_file_path = "critical_meters.glm"

    extract_meters(input_file_path, output_file_path)
