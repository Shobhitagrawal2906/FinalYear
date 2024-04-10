import cv2
from shapely import Point
from constants import constant_fps

class ObjectTracker:
    def __init__(self,manager,id) -> None:
        
        self.id = int(id)
        self.parent_manager = manager
        self.missing_counter = 0
        self.previous_location = None
        
        self.flag = False
        self.counter = 0
    
    def missing_object(self):
        
        self.missing_counter -= 1
        if self.missing_counter == 25:
            return True
    
    def find_location(self,frame,data):
        
        x,y,_,_ = data
        point = Point(x,y)
        location = "out"
        
        if point.within(self.parent_manager.down_in):
            location = "down_in"
        
        elif point.within(self.parent_manager.down_out):
            location = "down_out"
        
        elif point.within(self.parent_manager.up_in):
            location = "up_in"
        
        elif point.within(self.parent_manager.up_out):
            location = "up_out"
        
        self.track_movement(x,y,location,frame)
        
    def track_movement(self,x,y,location,frame):
        
        if location == "out" and self.previous_location in ["down_in","up_in"]:
            self.flag = True
            
        elif location in ["down_out","up_out"] and self.previous_location == "out":
            
            if self.counter!=0:
                speed = round(((30 / (self.counter/constant_fps)) * 3.6),2)
                if speed>75:
                    path = "images/{}.png".format(int(((139*self.id)+(self.counter*constant_fps))*12546.899))
                    lane,_ = location.split('_')
                    self.parent_manager.database_object.entry(self.id,speed,lane,path)
                    cv2.circle(frame,(x,y),100,(255,0,0),5)
                    cv2.imwrite(path,frame)
            
            self.flag = False
        
        self.previous_location = location