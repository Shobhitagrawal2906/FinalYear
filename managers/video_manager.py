from threading import Thread
from constants import VIDEO,DEBUG_MODE
from managers.display_manager import DisplayManager
from managers.database_manager import DatabaseManager
from entities.video_object import VideoObject

class VideoManager:
    def __init__(self) -> None:
        
        DatabaseManager()
        self.video = VideoObject(VIDEO)
        self.threading()
    
    def threading(self):
        
        thread = Thread(target=self.video.read_frames)
        thread.start()
        
        if DEBUG_MODE:    
            display_object = DisplayManager(self.video)
            display_object.display_frames()