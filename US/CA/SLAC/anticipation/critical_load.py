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


def find_meters(input):
	critical_meters = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])
				
	write_list_to_glm(critical_meters,'critical_meters.glm')
	obj_island_1=extract_objects('groups.glm', 'island_1')
	print(obj_island_1)

if __name__ == "__main__":
	find_meters(sys.argv[1])





	
