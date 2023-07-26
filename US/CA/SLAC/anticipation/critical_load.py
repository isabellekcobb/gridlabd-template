import pandas as pd
import gridlabd
import atexit

# Define a function to process the data after the simulation is completed
def process_data():
    services = []

    # Use 'meter' as the type argument to get objects of the 'meter' class
    objects = gridlabd.get_class('pole')

    for index, value in objects.items():
        child_obj = gridlabd.get_value(value, 'child')
        if gridlabd.get_class(child_obj) == 'meter':
            critical_level = gridlabd.get_value(child_obj, 'service_level')
            services.append(critical_level)
        else:
            services.append(0)

    # Convert the 'services' list to a DataFrame and save it to a CSV file
    df = pd.DataFrame({'service level': services})
    df.to_csv('service_level.csv', index=False)

# Register the process_data() function to run when the Python script exits
atexit.register(process_data)

# Load the GridLAB-D model (network.glm) and start the GridLAB-D simulation
gridlabd.command('network.glm')
gridlabd.start()
