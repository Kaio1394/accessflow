from accessflow.utils.access_utils import AccessUtils
from accessflow.utils.excel_utils import ExcelUtils
from accessflow.exceptions.errors import EmptyDataTable

class Docmd:
    def __init__(self, excel_utils: ExcelUtils, access_utils: AccessUtils):
        self.excel = excel_utils
        self.access = access_utils
        
    def transfer_spreadsheet(self):
        data_table = self.excel.read_worksheet()
        if not data_table:
            raise EmptyDataTable()