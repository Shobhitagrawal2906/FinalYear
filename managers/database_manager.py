from datetime import datetime
import pymongo
from constants import host,port,db,collection,DEBUG_MODE

class DatabaseManager:
    
    _instance = None
    def __init__(self) -> None:
        
        if DatabaseManager._instance is None:
            DatabaseManager._instance = self
        
        else:
            raise("Database Manager is a singleton class! Aborting.")

        self.client = pymongo.MongoClient(host,port)
        self.collection = self.client[db][collection]

    def entry(self,id,speed,lane,path):
        
        if DEBUG_MODE is False:
           
            try:
                
                self.collection.insert_one(
                    {
                        "CAR-ID" : int(id),
                        "Speed (KM/hr)"  : float(speed),
                        "Lane"   : lane,
                        "Image Path" : path,
                        "DB Entry Timestamp" : datetime.now()
                    }
                )
            
            except:
                raise("Some error occured while making database entry! Aborting...X")
        
        return
    
    @staticmethod
    def get_instance():
        return DatabaseManager._instance