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


def find_meters(input):
	critical_meters = []
	critical_objs = []
	critical_data = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])
				critical_island=find_island(model['objects'][obj]['parent'], 'groups.glm')
				objs=extract_objects('groups.glm', critical_island)
		for name in objs:
			if model['objects'][obj]['name']==name:
				critical_data.append(model['objects'][obj][data])
				
	write_list_to_glm(critical_data, 'critical_data.glm')			

input_glm=sys.argv[1]
if __name__ == "__main__":
	find_meters(input_glm)
