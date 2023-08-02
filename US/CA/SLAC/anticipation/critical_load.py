def critical_meters(input_file):
	#
	# Load model
	#
	with open(input_file,"r") as fh:
		model = json.load(fh)

	#
	# Check meter service_level
	#
        obj_list=[]
		for obj,data in model['objects'].items():
			obj_list.append(obj)

	obj_list.to_csv('objects.csv')


critical_meters('123.json')
