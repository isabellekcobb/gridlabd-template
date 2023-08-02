import sys, os
import json
import csv

def find_meters(input):
	critical_meters = []
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			if model['objects'][obj]['service_level']=='CRITICAL':
				critical_meters.append(model['objects'][obj])

	critical_meters.to_csv('critical_meters.csv')

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
