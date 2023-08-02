import sys, os
import json

def find_meters(input):
	with open(input,"r") as fh:
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		if data['class'].endswith('meter'):
			print(model['objects'][obj])

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
