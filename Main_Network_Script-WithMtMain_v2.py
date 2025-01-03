# STANDARD LIBRARY:
import ast
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, TimeoutError
from datetime import datetime
import logging
from pathlib import Path
from time import perf_counter, sleep
from numba import njit
import logging
import getpass

# 3RD PARTY LIBRARY
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
import xlwings as xw
from openpyxl import Workbook
from openpyxl import load_workbook
import json
import time

logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# LOCAL LIBRARY
# ---------------------

logging.basicConfig(filename="OUTPUT-LOG-FILE.txt", level=logging.DEBUG)

devices_dict = [{"CTKLx05": "10.61.184.5"}, {"CTKLx06": "10.61.184.6"}, {"CTKLx08": "10.61.184.8"}]

my_time = datetime.now().strftime("{H}%H-{M}%M-{S}%S".format(H='H', M='M', S='S'))
output_data = Path(__file__).parent / 'AUTOMATION_RULES1'
backup_data = "#FUTURE"
dataxlsmfile = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\JINJA\XLWINGS\demo\demo1.xlsm'


""" <DOC STRING HERE> """
def performance_counter(func):
    def script_tester(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        performance = finish - start
        print(f'Execution Time: {performance}')
    return script_tester


""" <DOC STRING HERE> """
class Switch_Function:
    def __init__(self, c_device_type: str, c_model: str, c_management_ip: str,
                 c_device_hostname: str, c_command: str, c_region: str,
                 c_country: str, c_site: str, c_my_device: str) -> None:
        self.device_type1 = c_device_type
        self.model1 = c_model
        self.management_ip1 = c_management_ip
        self.device_hostname1 = c_device_hostname
        self.command1 = c_command
        self.region = c_region
        self.country = c_country
        self.site = c_site
        self.my_device1 = c_my_device
        print(f'{self.device_hostname1}: {self.management_ip1} - Is being processed please wait for the result!')

    def Switch_Show_Cmd(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_multiline_timing(self.command1,
                                                               use_textfsm=False,
                                                               read_timeout=100,
                                                               delay_factor=40)
            sleep(5)
            return send_command_response
        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Unreachable or Cannot be accessed. Please check the device manually!'
            return x1

    def Switch_Cmd_json(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_command('show version', use_textfsm=True)
            device_hardware = send_command_response[0]['hardware'][0]
            device_serial = send_command_response[0]['serial'][0]
            return device_hardware, device_serial
        except Exception:
            device_hardware = 'UNKNOWN!'
            device_serial = 'UNKNOWN!'
            return device_hardware, device_serial

    def Switch_Change_Cmd(self):
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_config_response = conn.send_config_set(self.command1)
            return send_config_response

        except Exception:
            print("Device Unreachable!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - DEVICE2 Might be Offline, Unreachable or cannot inaccessible. Please check the device manually!\n'\
                'OR, Check if the VALUE used for the CHANGE "COMMAND" is good'
            return x1


class Firewall_Function(Switch_Function):
    def __init__(self, c_device_type, c_model, c_management_ip,
                 c_device_hostname, c_command, c_region, c_country, c_site, c_my_device):
        super().__init__(c_device_type, c_model, c_management_ip,
                         c_device_hostname, c_command, c_region, c_country, c_site, c_my_device)

    def Firewall_Show_Cmd(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_multiline(self.command1,
                                                        use_textfsm=False)
            return send_command_response
        except Exception:
            print("***********One or More device/s have ERROR! Please Check your CLI command and/or reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be offline, Invalid CLI command, Unreachable, or cannot inaccessible. Please check the device manually!'
            return x1

    def Firewall_Cmd_json(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1, allow_auto_change=True)
            conn.enable()
            send_command_response = conn.send_command("show inventory",
                                                      use_textfsm=True)
            device_hardware = send_command_response[0]['pid']
            device_serial = send_command_response[0]['sn']
            return device_hardware, device_serial
        except Exception:
            device_hardware = 'UKNOWN!'
            device_serial = 'UNKNOWN!'
            return device_hardware, device_serial

    def Firewall_Change_Cmd(self):
        try:
            conn = ConnectHandler(**self.my_device1, allow_auto_change=True)
            conn.enable()
            send_config_response = conn.send_config_set(self.command1)
            return send_config_response

        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Unreachable or Cannot be accessed. Please check the device manually!\n'\
                'OR, Check if the VALUE used for the CHANGE "COMMAND" is good'
            return x1

class WLC_Function(Switch_Function):
    def __init__(self, c_device_type, c_model, c_management_ip,
                 c_device_hostname, c_command, c_region, c_country, c_site, c_my_device):
        super().__init__(c_device_type, c_model, c_management_ip,
                         c_device_hostname, c_command, c_region, c_country, c_site, c_my_device)

    def WLC_Show_Cmd(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_multiline(self.command1,
                                                        use_textfsm=False)
            return send_command_response
        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Command not working, Unreachable or Cannot be accessed. Please check the device manually!'
            return x1

    def WLC_Cmd_json(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_command('show version',
                                                      use_textfsm=True)
            device_hardware = send_command_response[0]['hardware'][0]
            device_serial = send_command_response[0]['serial'][0]
            return device_hardware, device_serial
        except Exception:
            device_hardware = 'UKNOWN!'
            device_serial = 'UNKNOWN!'
            return device_hardware, device_serial

    def WLC_Change_Cmd(self):
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_config_response = conn.send_config_set(self.command1)
            return send_config_response

        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Unreachable or Cannot be accessed. Please check the device manually!\n'\
                'OR, Check if the VALUE used for the CHANGE "COMMAND" is good'
            return x1

class VOICE_GATEWAY_Function(Switch_Function):
    def __init__(self, c_device_type, c_model, c_management_ip,
                 c_device_hostname, c_command, c_region, c_country, c_site, c_my_device):
        super().__init__(c_device_type, c_model, c_management_ip,
                         c_device_hostname, c_command, c_region, c_country, c_site, c_my_device)

    def VG_Show_Cmd(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_multiline(self.command1,
                                                        use_textfsm=False)
            return send_command_response
        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Command not working, Unreachable or Cannot be accessed. Please check the device manually!'
            return x1

    def VG_Cmd_json(self: str) -> str:
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_command_response = conn.send_command('show version',
                                                      use_textfsm=True)
            device_hardware = send_command_response[0]['hardware'][0]
            device_serial = send_command_response[0]['serial'][0]
            return device_hardware, device_serial
        except Exception:
            device_hardware = 'UKNOWN!'
            device_serial = 'UNKNOWN!'
            return device_hardware, device_serial

    def VG_Change_Cmd(self):
        try:
            conn = ConnectHandler(**self.my_device1)
            conn.enable()
            send_config_response = conn.send_config_set(self.command1)
#            conn.disconnect()
            return send_config_response

        except Exception:
            print("***********One or More device/s have ERROR! Please Check its reachability!")
            x1 = f'{self.device_hostname1}: {self.management_ip1} - Might be Offline, Unreachable or Cannot be accessed. Please check the device manually!\n'\
                'OR, Check if the VALUE used for the CHANGE "COMMAND" is good'
            return x1

"""
Jinja_Template: To be used if a SPECIAL output FORMAT is needed in combination
For the returned netmiko output.
"""


def Jinja_Template(netmiko_output: str, switch_class1: str, serial_and_version) -> str:
    template_location = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\PROJECT\SHOWOFF\template'
    env = Environment(loader=FileSystemLoader(template_location), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('Jinja_Template_HTML.j2')
    jinja_output = template.render(SHOW_OR_CHANGE_OUTPUT=netmiko_output,
                                   DEVICE_HOSTNAME=switch_class1.device_hostname1,
                                   MANAGEMENT_IP=switch_class1.management_ip1,
                                   COMMAND=switch_class1.command1,
                                   REGION=switch_class1.region,
                                   COUNTRY=switch_class1.country,
                                   SITE=switch_class1.site,
                                   DEVICE_TYPE=switch_class1.device_type1,
                                   DEVICE_HARDWARE=serial_and_version[0],
                                   DEVICE_SERIAL=serial_and_version[1])
    return jinja_output


def Jinja_Template_Exception() -> str:
    main_template = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\PROJECT\SHOWOFF\template'
    env = Environment(loader=FileSystemLoader(main_template), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('Jinja_Template_Exception.j2')
    jinja_output = template.render()
    return jinja_output


start = perf_counter()


class main_information():
    @xw.func
    def __init__(self, password1: str):
        """
        test
        """
        wb = xw.Book.caller()
        sheet = wb.sheets[0]
        excel_value = sheet.range('B2:C1048576', 'B11:C16').value
        dict_data_value = {rows[0]: rows[1] for rows in excel_value}
        self.v_username = str(dict_data_value['USERNAME'])
        self.v_device_type = str(dict_data_value['DEVICE_TYPE'])
        self.v_model = str(dict_data_value['NETWORK'])
        self.v_hostname_ip = ast.literal_eval(dict_data_value['HOSTNAME_IP'])
        self.v_show_or_change = str(dict_data_value['SHOW_OR_CHANGE'])
        self.v_device_hostname = str(dict_data_value['DEVICE_HOSTNAME'])
        self.v_password = str(password1)
        self.v_secret = str(password1)
        self.v_command = str(dict_data_value['COMMAND']).split(",")
        self.v_region = str(dict_data_value['REGION'])
        self.v_country = str(dict_data_value['COUNTRY'])
        self.v_site = str(dict_data_value['SITE'])

    def code(self, hostname_ip):
        for f_host, f_ip in hostname_ip.items():
            DEVICE_NETMIKO_IOS = {
                "session_log": 'netmiko_session.log',
                'host': f_ip,
                'port': 22,
                'conn_timeout': 10,
                'username': self.v_username,
                'password': self.v_password,
                'secret': self.v_secret,
                'fast_cli': False,
                'device_type': "cisco_ios",
            }
            DEVICE_NETMIKO_AIROS = {
                "session_log": 'netmiko_session.log',
                'host': f_ip,
                'port': 22,
                'username': self.v_username,
                'password': self.v_password,
                'device_type': "cisco_wlc_ssh",
            }

            """ <DOC STRING HERE> """
            if self.v_device_type == str('switch').upper():
                if self.v_show_or_change == str('show').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    switch_class1 = Switch_Function(self.v_device_type,
                                                    self.v_model,
                                                    management_ip,
                                                    device_hostname,
                                                    self.v_command,
                                                    self.v_region,
                                                    self.v_country,
                                                    self.v_site,
                                                    DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(switch_class1.Switch_Show_Cmd(),
                                                       switch_class1, switch_class1.Switch_Cmd_json())

                elif self.v_show_or_change == str('change').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    switch_class1 = Switch_Function(self.v_device_type,
                                                    self.v_model,
                                                    management_ip,
                                                    device_hostname,
                                                    self.v_command,
                                                    self.v_region,
                                                    self.v_country,
                                                    self.v_site,
                                                    DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(switch_class1.Switch_Change_Cmd(),
                                                       switch_class1, switch_class1.Switch_Cmd_json())

            elif self.v_device_type == str('firewall').upper():
                if self.v_show_or_change == str('show').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    firewall_class1 = Firewall_Function(self.v_device_type,
                                                        self.v_model,
                                                        management_ip,
                                                        device_hostname,
                                                        self.v_command,
                                                        self.v_region,
                                                        self.v_country,
                                                        self.v_site,
                                                        DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(firewall_class1.Firewall_Show_Cmd(),
                                                       firewall_class1, firewall_class1.Firewall_Cmd_json())
                elif self.v_show_or_change == str('change').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    firewall_class1 = Firewall_Function(self.v_device_type,
                                                        self.v_model,
                                                        management_ip,
                                                        device_hostname,
                                                        self.v_command,
                                                        self.v_region,
                                                        self.v_country,
                                                        self.v_site,
                                                        DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(firewall_class1.Firewall_Change_Cmd(),
                                                       firewall_class1, firewall_class1.Firewall_Cmd_json())
            elif self.v_device_type == str('wlc').upper():
                if self.v_show_or_change == str('show').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    wlc_class1 = WLC_Function(self.v_device_type,
                                              self.v_model,
                                              management_ip,
                                              device_hostname,
                                              self.v_command,
                                              self.v_region,
                                              self.v_country,
                                              self.v_site,
                                              DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(wlc_class1.WLC_Show_Cmd(),
                                                       wlc_class1, wlc_class1.WLC_Cmd_json())
                elif self.v_show_or_change == str('change').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    wlc_class1 = WLC_Function(self.v_device_type,
                                              self.v_model,
                                              management_ip,
                                              device_hostname,
                                              self.v_command,
                                              self.v_region,
                                              self.v_country,
                                              self.v_site,
                                              DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(wlc_class1.WLC_Change_Cmd(),
                                                       wlc_class1, wlc_class1.WLC_Cmd_json())                  
            elif self.v_device_type == str('wlc_airos').upper():
                if self.v_show_or_change == str('show').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_AIROS['host']
                    wlc_class1 = WLC_Function(self.v_device_type,
                                              self.v_model,
                                              management_ip,
                                              device_hostname,
                                              self.v_command,
                                              self.v_region,
                                              self.v_country,
                                              self.v_site,
                                              DEVICE_NETMIKO_AIROS)
                    output_writefile1 = Jinja_Template(wlc_class1.WLC_Show_Cmd(),
                                                       wlc_class1, wlc_class1.WLC_Cmd_json())
                elif self.v_show_or_change == str('change').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_AIROS['host']
                    wlc_class1 = WLC_Function(self.v_device_type,
                                              self.v_model,
                                              management_ip,
                                              device_hostname,
                                              self.v_command,
                                              self.v_region,
                                              self.v_country,
                                              self.v_site,
                                              DEVICE_NETMIKO_AIROS)
                    output_writefile1 = Jinja_Template(wlc_class1.WLC_Change_Cmd(),
                                                       wlc_class1, wlc_class1.WLC_Cmd_json()) 
            elif self.v_device_type == str('voice_gateway').upper():
                if self.v_show_or_change == str('show').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    wlc_class1 = VOICE_GATEWAY_Function(self.v_device_type,
                                                        self.v_model,
                                                        management_ip,
                                                        device_hostname,
                                                        self.v_command,
                                                        self.v_region,
                                                        self.v_country,
                                                        self.v_site,
                                                        DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(wlc_class1.VG_Show_Cmd(),
                                                       wlc_class1, wlc_class1.VG_Cmd_json())
                elif self.v_show_or_change == str('change').upper():
                    device_hostname = f_host
                    management_ip = DEVICE_NETMIKO_IOS['host']
                    wlc_class1 = VOICE_GATEWAY_Function(self.v_device_type,
                                                        self.v_model,
                                                        management_ip,
                                                        device_hostname,
                                                        self.v_command,
                                                        self.v_region,
                                                        self.v_country,
                                                        self.v_site,
                                                        DEVICE_NETMIKO_IOS)
                    output_writefile1 = Jinja_Template(wlc_class1.VG_Change_Cmd(),
                                                       wlc_class1, wlc_class1.VG_Cmd_json()) 

            else:
                print('ERROR! Please check the PROGRAM/EXCEL!')
            return output_writefile1


if __name__ == "__main__":
    xw.Book("Main_Template.xlsm").set_mock_caller()
#    try:
    with open("3HTML_TESTING.html", 'w') as writefile:
        sure_change1 = input(f"are you sure you want to proceed with the command:\n\t {main_information(getpass).v_command}? PLEASE DOUBLE CHECK! (yes/no):")
        if sure_change1 == str('yes') or sure_change1 == str('YES') or sure_change1 == str('Y') or sure_change1 == str('y'):
            password1 = getpass.getpass(prompt="Enter your TACACS password: ")
            combine_codes = main_information(getpass)
            with ThreadPoolExecutor(max_workers=500) as executor:
                multi_threading_results = executor.map(main_information(password1).code,
                                                       main_information(password1).
                                                       v_hostname_ip,
                                                       timeout=5)
                exec_result = executor.shutdown(wait=True,
                                                cancel_futures=True)

            for multi_threading_output in multi_threading_results:
                writefile.write(multi_threading_output)

        elif sure_change1 == str('no') or sure_change1 == str('NO') or sure_change1 == str('N') or sure_change1 == str('n'):
            print('Confirmed... Exiting Script! Have a good day! :)')
            time.sleep()
            exit()

        else:
            with TimeoutError() as error:
                raise error("Input could not be recognized! Please run the program once again.")

        end = perf_counter()
        total_time = end - start
        print(f'Time processed the request: {total_time}')
        writefile.close()
#    except Exception:
#        with open("1NETMIKO_OUTPUT.txt", 'w') as writefile1:
#            jte1 = Jinja_Template_Exception()
#            print(jte1)
#            writefile1.write(str(jte1))
#            writefile1.close()
#            end = perf_counter()
#            total_time = end - start
#            print(f'Time processed the request: {total_time}')            
#            end = perf_counter()