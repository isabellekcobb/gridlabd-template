import sys, os
import json
import csv
import re

def write_list_to_glm(data_list, file_name):
    with open(file_name, mode='w') as file:
        for item in data_list:
            file.write(str(item) + '\n')
		
def extract_objects(file_path, group_name):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regex to find the groups dictionary
    groups_match = re.search(r'groups\s*=\s*({[^}]*})', content)

    if not groups_match:
        raise ValueError("No 'groups' dictionary found in the .glm file.")

    groups_str = groups_match.group(1)
    groups = eval(groups_str)  # Convert the matched string to a dictionary using eval

    if group_name not in groups:
        raise ValueError(f"Group '{group_name}' not found in the .glm file.")

    return groups[group_name]

def find_island(node_name, file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regex to find the groups dictionary
    groups_match = re.search(r'groups\s*=\s*({[^}]*})', content)

    if not groups_match:
        raise ValueError("No 'groups' dictionary found in the .glm file.")

    groups_str = groups_match.group(1)
    groups = eval(groups_str)  # Convert the matched string to a dictionary using eval

    # Loop through all groups and find the one containing the node_name
    for group_name, objects_list in groups.items():
        if node_name in objects_list:
            return group_name

    # If the node_name is not found in any group, it's not assigned to any island.
    return None

import re

def extract_object_data(file_path, object_names):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    extracted_data = {}

    for object_name in object_names:
        regex = re.compile(rf"object\s+{object_name}\s*{{(.*?)}}", re.DOTALL)
        match = regex.search(file_content)

        if match:
            object_data = match.group(1).strip()
            extracted_data[object_name] = object_data
        else:
            print(f"Object not found: {object_name}")

    return extracted_data

def find_meters(input):
	critical_meters = []
	critical_objs = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])
				critical_island=find_island(model['objects'][obj]['parent'], 'groups.glm')
				objs=extract_objects('groups.glm', critical_island)
				critical_objs.append(objs)
	return critical_objs

input_glm=sys.argv[1]
if __name__ == "__main__":
	input_array=find_meters(input_glm)
	extract_object_data(input_glm, input_array)
