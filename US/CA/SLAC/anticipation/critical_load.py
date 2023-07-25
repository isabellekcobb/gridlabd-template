import os
import gridlabd
def on_finish():
  objects=gridlabd.get(object)
  meters_list=[]
  for index,value in objects:
      if gridlabd.get_class(value)=='meter':
        meters_list.append(value)
        parent_obj=gridlabd.get_value(value,parent)
        if gridlabd.get_class(parent_obj)=='pole':
          
      
        
          
          

  
