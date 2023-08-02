import sys, os
import json

def find_meters(input):
	critical_meters = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])

	output_file_path = "critical_meters.glm"
	with open(output_file_path, mode='w') as file:
    		for line in critical_meters:
        		file.write(line)

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
