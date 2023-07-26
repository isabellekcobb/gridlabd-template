import pandas as pd
import gridlabd
import atexit

# Define a function to process the data after the simulation is completed
def process_data():
    services = []

    # Use 'meter' as the type argument to get objects of the 'meter' class
    objects = gridlabd.get(objects)
    
    for index, value in objects.items():
        if gridlabd.get_class(value) == 'meter':
            parent_obj = gridlabd.get_value(value, 'parent')
            if gridlabd.get_class(parent_obj) == 'pole':
                critical_level = gridlabd.get_value(value, 'service_level')
                services.append(critical_level)
            else:
                services.append(0)

    # Convert the 'services' list to a DataFrame and save it to a CSV file
    df = pd.DataFrame({'service level': services})
    df.to_csv('service_level.csv', index=False)

# Define a function to run the gridlabd command during the on_compile event
def on_init():
    gridlabd.command('network.glm')

# Register the process_data() function to run after the simulation is completed
atexit.register(process_data)

# Now, call the on_compile() function to initiate the process
on_init()

