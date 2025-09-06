from accessflow.utils.access_utils import AccessUtils
from accessflow.utils.excel_utils import ExcelUtils
import pyodbc

if '__main__' == __name__:
    try:
        # print(pyodbc.drivers())
        # access = AccessUtils("C:\\access_teste\\accessflow.accdb")
        # its_work, msg_error = access.test_connection()
        # if not its_work:
        #     print('Failed connection.')
        # else:
        #     print('Connection successfull.')
        # access.connect()
        # data_table = access.read_sql('SELECT * FROM table_test;')
        
        excel_utils = ExcelUtils('C:\\access_teste\\teste.xlsx')
        excel_utils.open()
        excel_utils.set_worksheet('name')
        data_table = excel_utils.read_workworksheet('name')
        
    finally:
        # access.disconnect()
        excel_utils.close()