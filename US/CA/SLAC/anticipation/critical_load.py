def find_meters(input)
	obj_lis = []
	with open(input,"r") as fh:
		model=json.load(fh)

	for obj,data in model['objects'].items():
		print(model['objects'][obj])

if __name__ == "__main__":
	find_meters(sys.argv[1])
	
