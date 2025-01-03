from concurrent.futures import ThreadPoolExecutor
from jinja2 import Environment, FileSystemLoader
from time import perf_counter
from netmiko import ConnectHandler
import xlwings as xw
import ast
import json

class Switch_Function:
    def __init__(self, c_device_type: str, c_model: str, c_management_ip: str,
                 c_device_hostname: str, c_command: str, c_my_device: str):
        self.device_type1 = c_device_type
        self.model1 = c_model
        self.management_ip1 = c_management_ip
        self.device_hostname1 = c_device_hostname
        self.command1 = c_command
        self.my_device1 = c_my_device
        print(self.my_device1)

    def Switch_Show_Cmd(self: str) -> str:
        conn = ConnectHandler(**self.my_device1)
        conn.enable()
        send_command_response = conn.send_command(self.command1,
                                                  use_textfsm=False)
#        json_response = json.dumps(x222, indent=2)
#        output_response = json_response.replace('\\n', '\n').replace('\\t', '\t')
#        x123 = output_response["software_image"]
        conn.disconnect()
        return send_command_response

def Jinja_Template(netmiko_output: str, switch_class1: str) -> str:
    main_template = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\PROJECT\SHOWOFF\template'
    env = Environment(loader=FileSystemLoader(main_template), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('Jinja_Template.j2')
    jinja_output = template.render(SHOW_OR_CHANGE_OUTPUT=netmiko_output,
                                   DEVICE_HOSTNAME=switch_class1.device_hostname1,
                                   MANAGEMENT_IP=switch_class1.management_ip1,
                                   COMMAND=switch_class1.command1)
    return jinja_output


@xw.func
def main():
    """
    <DOCT-STRING HERE>
    """
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    username = sheet.range('B2:C16').value
    dict_data_value = {rows[0]: rows[1] for rows in username}
    v_username = str(dict_data_value['USERNAME'])
    with open("1CSV_OUTPUT-TEST.txt", 'w') as writefile:
        excel_value = sheet.range('B2:C1048576', 'B11:C16').value
        dict_data_value = {rows[0]: rows[1] for rows in excel_value}
        v_device_type = dict_data_value['DEVICE_TYPE']
        v_model = dict_data_value['MODEL']
        v_hostname_ip = ast.literal_eval(dict_data_value['HOSTNAME_IP'])
        print(v_hostname_ip)
        v_show_or_change = str(dict_data_value['SHOW_OR_CHANGE'])
        v_device_hostname = str(dict_data_value['DEVICE_HOSTNAME'])
        v_password = str(dict_data_value['PASSWORD_HIDDEN'])
        v_secret = str(dict_data_value['SECRET_HIDDEN'])
        v_command = str(dict_data_value['COMMAND'])

        for x1 in v_hostname_ip:
            for f_host, f_ip in x1.items():
                DEVICE_NETMIKO = {
                    'host': f_ip,
                    'port': 22,
                    'username': v_username,
                    'password': v_password,
                    'secret': v_secret,
                    'device_type': "cisco_ios",
                }

                """ <DOC STRING HERE> """
                if v_device_type == str('switch').upper() and v_model == str('c9000-switch').upper():
                    if v_show_or_change == str('show').upper():
                        device_hostname = f_host
                        management_ip = DEVICE_NETMIKO['host']
                        switch_class1 = Switch_Function(v_device_type, v_model,
                                                        management_ip,
                                                        device_hostname,
                                                        v_command,
                                                        DEVICE_NETMIKO)
                        netmiko_output = switch_class1.Switch_Show_Cmd()
                        output_writefile1 = Jinja_Template(netmiko_output,
                                                        switch_class1)
                else:
                    print('ERROR! Please check the PROGRAM/EXCEL!')

                writefile.write(output_writefile1)

if __name__ == "__main__":
    xw.Book("Main_Template.xlsm").set_mock_caller()
    main()