import pandas as pd
import gridlabd


def on_term():
    gridlabd.command('network.glm')
    services = []

    # Use 'meter' as the type argument to get objects of the 'meter' class
    obj_list = gridlabd.get(objects)
    
    for index, value in obj_list.items():
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
    

