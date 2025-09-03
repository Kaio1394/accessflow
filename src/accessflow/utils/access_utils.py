import pyodbc
import os
import pandas as pd
from accessflow.constants.general import DRIVER_ACCESS
from accessflow.core.types import DataTable, dataframe_to_datatable

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
        
    def test_connection(self) -> tuple[bool, str]:
        try:
            self.connect()
            if self._conn:
                self.disconnect()
            return True, ""
        except Exception as err:
            return False, str(err)
    
    def commit(self):
        if self._conn is not None:
            self._conn.commit()
            
    def execute_query(self, query) -> DataTable:
        dataframe = pd.read_sql(query, self._conn)
        data_table = dataframe_to_datatable(dataframe)
        return data_table
    
    def disconnect(self):
        if self._conn is not None:
            self._conn.close()
            
    