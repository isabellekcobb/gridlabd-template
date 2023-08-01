import gridlabd

def get_all_meters(glm_file_path):
    meter_names = []
    with open(glm_file_path, 'r') as f:
        glm_content = f.read()
        obj_list=gridlabd.get("objects")
        for i in obj_list:
            if gridlabd.get_value(i,"class")=="meter":
                meter_names.append(i)
        

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
