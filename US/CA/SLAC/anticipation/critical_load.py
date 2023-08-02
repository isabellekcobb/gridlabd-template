def find_meters(input):
	with open(input,"r") as fh:
		model=json.load(fh)

	for obj,data in model['objects'].items():
		print(model['objects'][obj]['name'])

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
