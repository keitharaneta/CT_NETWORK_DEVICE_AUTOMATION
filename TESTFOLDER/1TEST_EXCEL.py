import xlwings as xw
from pathlib import Path
import pandas as pd
from scrapli.driver.core import IOSXEDriver
from netmiko import ConnectHandler
import ast

output_data = Path(__file__).parent / 'AUTOMATION_RULES1.txt'
dataxlsmfile = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\JINJA\XLWINGS\demo\demo1.xlsm'

@xw.func
def main():
    with open(output_data, 'w') as writefile:
        wb = xw.Book.caller()
        sheet = wb.sheets[0]
        excel_value = sheet.range('B2:C9', 'B11:C16').value
        dict_data_value = {rows[0]: rows[1] for rows in excel_value}
        print(dict_data_value)
        v_device_type = dict_data_value['DEVICE_TYPE']
        v_model = dict_data_value['MODEL']
        v_hostname_ip = ast.literal_eval(str(dict_data_value['HOSTNAME_IP']))
        v_show_or_change = dict_data_value['SHOW_OR_CHANGE']
        v_command = str(dict_data_value['COMMAND'])
        

if __name__ == "__main__":
    xw.Book("Main_Template.xlsm").set_mock_caller()
    main()