import cv2
import numpy as np
from queue import Queue
from managers.detection_manager import DetectionManager
import yolo 
from constants import DEBUG_MODE,red,green,blue,orange

class VideoObject:
    def __init__(self,link) -> None:
        
        self.link = link
        self.video = cv2.VideoCapture(self.link)
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.model = yolo.YOLOModel()
        self.detect = DetectionManager()
        
        if DEBUG_MODE:
            self.writer = Queue(maxsize=1)
    
    def draw_roi(self,frame):
        
        colors = [red,green,blue,orange]
        i=0
        for value in self.detect.ROI: 
            x,y = value[0].exterior.coords.xy
            points = np.array([point for point in list(zip(x,y))]).astype(int)
            frame = cv2.polylines(frame,[np.int32(points)],True,colors[i],4)
            i+=1
        
        return frame
    
    def read_frames(self):

        while True:
            ret,frame = self.video.read()
            
            if ret:
                
                results = self.model.model1.track(frame,persist = True,verbose = False)
                for result in results:
                    
                    frame_data = {}
                    if result.boxes.id is None: continue
                    
                    ids = (result.boxes.id).numpy().astype(int)
                    coords = (result.boxes.xywh).numpy().astype(int)
                    
                    for id,coord in zip(ids,coords):
                        frame_data[id] = coord
                    
                    if DEBUG_MODE:
                        
                        frame = self.draw_roi(frame)
                        frame = result.plot()
                        self.writer.put(frame)

                    self.detect.track_objects(frame,frame_data)
            else:
                break
            
        
        cv2.destroyAllWindows()
        self.video.release()