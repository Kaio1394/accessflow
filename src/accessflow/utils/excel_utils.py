import openpyxl
import os
from accessflow.core.types import DataTable

class ExcelUtils:
    def __init__(self, path_excel: str, tab_name: str, has_header: bool = True):
        if not path_excel or not path_excel.strip():
           raise ValueError('Invalid value: string <path_excel> is empty.')   
        if not tab_name or not tab_name.strip():
           raise ValueError('Invalid value: string <tab_name> is empty.') 
        if not os.path.isfile(path_excel):
            raise FileNotFoundError(f'The Excel [{path_excel}] File not found.')
        self.path_excel = path_excel
        self.tab_name = tab_name
        self.has_header = has_header
    
    def open(self):
        pass  
    
    def read_worksheet(self) -> DataTable:
        pass  
    
    def close(self):
        pass