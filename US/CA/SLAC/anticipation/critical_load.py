import sys, os
import json
import csv

def write_list_to_csv(data_list, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)
	    
def find_meters(input):
	critical_meters = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])
				
	write_list_to_csv(critical_meters,'critical_meters.csv')

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
