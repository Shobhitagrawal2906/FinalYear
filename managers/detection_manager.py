from shapely import Polygon
from json import load
from constants import DEBUG_MODE,JSON
from entities.object_tracker import ObjectTracker
from managers.database_manager import DatabaseManager

class DetectionManager:
     def __init__(self) -> None:
          
          self.tracked = dict()
          self.old = dict()
       
          try:
               self.json_data = load(open(JSON))
       
          except:
               raise("Error while loading JSON file. Check path/name/directory and try again. Exiting()")     
        
          self.database_object = DatabaseManager.get_instance()
          self.down_in = []
          self.down_out = []
          self.up_in = []
          self.up_out = []
          self.ROI = [self.down_in,self.down_out,self.up_in,self.up_out]
          
          self.get_roi()
          
     def get_roi(self):
          
          for data in self.json_data['boxes']:
               
               if data['label'] == 'Down-In':
                    self.down_in.append(Polygon(data['points']))
               if data['label'] == 'Down-Out':
                    self.down_out.append(Polygon(data['points']))
               if data['label'] == 'Up-In':
                    self.up_in.append(Polygon(data['points']))
               if data['label'] == 'Up-Out':
                    self.up_out.append(Polygon(data['points']))
     
     def track_objects(self,frame,current_frame):
          
          if not self.tracked:
            
            self.tracked = {object_id : ObjectTracker(self,object_id) for object_id in current_frame.keys()}
        
          else:
            
            currentcopy = current_frame.copy()
            trackedcopy = self.tracked.copy()
            
            for object in trackedcopy.keys():
                
                if object in current_frame:
                    
                    current_frame.pop(object)
                
                else:
                    
                    self.old[object] = self.tracked[object]
                    self.tracked.pop(object)
            
            currentcopysecond = current_frame.copy()
            for object in currentcopysecond:
                
                if object in self.old:
                    
                    self.tracked[object] = self.old[object]
                    self.tracked[object].missing_counter = 0
                    self.old.pop(object)
                    current_frame.pop(object)
                
                else:
                    self.tracked.update({object:ObjectTracker(self,object)})   
                
            trackedcopy = self.tracked.copy()
            for object in trackedcopy:
                if self.tracked[object].flag : self.tracked[object].counter += 1
                self.tracked[object].find_location(frame,currentcopy[object]) 
                
            oldcopy = self.old.copy()
            
            for object in oldcopy:
                
               if self.old[object].missing_object(): 
                    del self.old[object]