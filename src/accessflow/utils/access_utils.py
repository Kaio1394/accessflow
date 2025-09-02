import pyodbc
import os
from accessflow.constants.general import DBQ, DRIVER_ACCESS

class AccessUtils:
    def __init__(self, path_file_access):   
        if not path_file_access or not path_file_access.strip():
           raise ValueError('Invalid value: string is empty.')    
        if not os.path.isfile(path_file_access):
            raise FileNotFoundError(f'The Access [{path_file_access}] File not found.')
        self.path_file_access = path_file_access
        self._conn = None
        self._cursor = None
    
    def connect(self):
        conn_str = (
            f"{DRIVER_ACCESS}"
            f"DBQ={self.path_file_access};"
        )
        self._conn = pyodbc.connect(conn_str)
       
    def transfer_spreadsheet(self):
        pass
    
    def commit(self):
        if self._conn is not None:
            self._conn.commit()
    
    def disconnect(self):
        if self._conn is not None:
            self._conn.close()
            
    