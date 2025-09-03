from accessflow.utils.access_utils import AccessUtils
from accessflow.utils.excel_utils import ExcelUtils
from accessflow.exceptions.errors import EmptyDataTable

class Docmd:
    def __init__(self, path_access: str, path_excel: str, tab_name: str, has_header: bool = True):
        self.excel = ExcelUtils(path_excel, tab_name, has_header)
        self.access = AccessUtils(path_access)
        
    def transfer_spreadsheet(self):
        data_table = self.excel.read_worksheet()
        if not data_table:
            raise EmptyDataTable()