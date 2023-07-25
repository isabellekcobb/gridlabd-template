import os
import gridlabd
import csv
import pandas as pd

gridlabd.command('network.glm')

services=[]

objects=gridlabd.get('object')
for index,value in objects:
  if gridlabd.get_class(value)=='meter':
    parent_obj=gridlabd.get_value(value,parent)
    if gridlabd.get_class(parent_obj)=='pole':
      critical_level=gridlabd.get_value(value, service_level)
      services.append(critical_level)
    else:
      services.append(0)

services.to_csv('service_level.csv', index=False)
          
          
      
        
          
          

  
