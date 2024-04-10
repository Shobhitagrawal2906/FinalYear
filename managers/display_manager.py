import cv2
import time

class DisplayManager:
    def __init__(self,link) -> None:
        self.video = link
    
    def display_frames(self):
        
        while True:
            
            if self.video.writer.empty():
                time.sleep(0.001)
                continue
        
            frame = self.video.writer.get()
            cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('frame',(900,600))
            cv2.imshow('frame',frame)
        
            cv2.waitKey(int(self.video.fps))