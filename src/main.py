from accessflow.utils.access_utils import AccessUtils
import pyodbc

if '__main__' == __name__:
    try:
        print(pyodbc.drivers())
        access = AccessUtils("C:\\access_teste\\accessflow.accdb")
        its_work, msg_error = access.test_connection()
        if not its_work:
            print('Failed connection.')
        else:
            print('Connection successfull.')
        access.connect()
        data_table = access.execute_query('SELECT * FROM table_test;')
        
    finally:
        access.disconnect()