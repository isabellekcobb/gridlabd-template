import sys, os
import json

print('check 1')
def find_meters(input):
	print('check 3')
	with open(input,"r") as fh:
		print('check 4')
		model=json.load(fh)
	
	for obj,data in model['objects'].items():
		print('check 5')
		print(model['objects'][obj])

if __name__ == "__main__":
	print('check 2')
	find_meters(sys.argv[1])
	
