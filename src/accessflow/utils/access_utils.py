import pyodbc
import os
from src.constants.general import DRIVER_ACCESS, DBQ

class AccessUtils:
    def __init__(self, path_file_access):        
        if not os.path.isfile(path_file_access):
            raise FileNotFoundError(f'The Access [{path_file_access}] File not found.')
        self.path_file_access = path_file_access
        self.conn = None
    
    def connect(self):
       self.conn = pyodbc.connect()
       
    def transfer_spreadsheet(self):
        pass
    
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            
    