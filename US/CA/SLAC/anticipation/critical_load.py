import os
import gridlabd
import csv
import pandas as pd

csv_input=pd.read_csv('path_result_plot.csv')
services=[]
def on_finish():
  objects=gridlabd.get(object)
  for index,value in objects:
      if gridlabd.get_class(value)=='meter':
        parent_obj=gridlabd.get_value(value,parent)
        if gridlabd.get_class(parent_obj)=='pole':
          critical_level=gridlabd.get_value(value, service_level)
          services.append(critical_level)
        elif:
          services.append(0)

csv_input['service level']=services
csv_input.to_csv('path_result_plot.csv', index=False)
          
          
      
        
          
          

  
