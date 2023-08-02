import sys, os
import json

print('check 1')
def find_meters(input):
	with open(input,"r") as fh:
		model=json.load(fh)
	print('check 3')
	for obj,data in model['objects'].items():
		print(model['objects'][obj]['name'])

	print('check 4')

if __name__ == "__main__":
	print('check 2')
	find_meters(sys.argv[1])
	
