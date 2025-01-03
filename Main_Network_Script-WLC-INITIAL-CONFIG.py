# STANDARD LIBRARY:
import ast
from datetime import datetime
import json
from pathlib import Path
from time import perf_counter

# 3RD PARTY LIBRARY
import csv
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
import xlwings as xw

# LOCAL LIBRARY

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


@performance_counter
@xw.func
def main():
    main_template = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\PROJECT\SHOWOFF\template'
    env = Environment(loader=FileSystemLoader(main_template), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('Jinja_Template_WLC_INITIAL_CONFIG.j2')

    wb = xw.Book.caller()
    sheet = wb.sheets[1]
    username = sheet.range('B2:C30').value
    dict_data_value = {rows[0]: rows[1] for rows in username}
    print(dict_data_value)
    local_var_time = my_time
    local_var_output_data = output_data
    with open("1WLC_JINJA_OUTPUT.csv", encoding='utf-8', mode='w') as writefile:
        excel_value = sheet.range('B2:C30').value
        dict_data_value = {rows[0]: rows[1] for rows in excel_value}
        print(dict_data_value)
        wlc_management = str(dict_data_value['WLC_MANAGEMENT'])
        wlc_management_subnet = str(dict_data_value['WLC_MANAGEMENT_SUBNET'])
        wlc_management_gateway = str(dict_data_value['WLC_MANAGEMENT_GATEWAY'])
        wlc_management_ha_unit = str(dict_data_value['WLC_MANAGEMENT_HA_UNIT'])
        wlc_management_ha_unit_subnet = str(dict_data_value['WLC_MANAGEMENT_HA_UNIT_SUBNET'])
        service_port_ip = str(dict_data_value['SERVICE_PORT_IP'])
        service_port_ip_gateway = str(dict_data_value['SERVICE_PORT_IP_GATEWAY'])
        service_port_subnet = str(dict_data_value['SERVICE_PORT_SUBNET'])
        wlan_g6_interface = str(dict_data_value['WLAN_G6_INTERFACE'])
        wlan_g6_subnet = str(dict_data_value['WLAN_G6_SUBNET'])
        wlan_g7_interface = str(dict_data_value['WLAN_G7_INTERFACE'])
        wlan_g7_subnet = str(dict_data_value['WLAN_G7_SUBNET'])
        wlan_g8_staging_interface = str(dict_data_value['WLAN_G8_STAGING_INTERFACE'])
        wlan_g8_staging_subnet = str(dict_data_value['WLAN_G8_STAGING_SUBNET'])
        wlan_g8_staging_gateway = str(dict_data_value['WLAN_G8_STAGING_GATEWAY'])
        wlan_g8_interface = str(dict_data_value['WLAN_G8_INTERFACE'])
        wlan_g8_subnet = str(dict_data_value['WLAN_G8_SUBNET'])
        corp_guest = str(dict_data_value['CORP_GUEST'])
        corp_guest_subnet = str(dict_data_value['CORP_GUEST_SUBNET'])
        redundancy_ip_primary = str(dict_data_value['REDUNDANCY_IP_PRIMARY'])
        redundancy_ip_ha_unit = str(dict_data_value['REDUNDANCY_IP_HA_UNIT'])
        dhcp_ip = str(dict_data_value['DHCP_IP'])
        wlc_name = str(dict_data_value['WLC_NAME'])
        vtp_domain = str(dict_data_value['VTP_DOMAIN'])
        snmp_location = str(dict_data_value['SNMP_LOCATION'])
        rf_network = str(dict_data_value['RF_NETWORK'])
        g7_re = str(dict_data_value['G7_RE'])
        ap_country = str(dict_data_value['AP_COUNTRY'])
        default_management_vlan = str(dict_data_value['DEFAULT_MANAGEMENT_VLAN'])

        jinja_output = template.render(WLC_MANAGEMENT=wlc_management,
                                       WLC_MANAGEMENT_SUBNET=wlc_management_subnet,
                                       WLC_MANAGEMENT_GATEWAY=wlc_management_gateway,
                                       WLC_MANAGEMENT_HA_UNIT=wlc_management_ha_unit,
                                       WLC_MANAGEMENT_HA_UNIT_SUBNET=wlc_management_ha_unit_subnet,
                                       SERVICE_PORT_IP=service_port_ip,
                                       SERVICE_PORT_IP_GATEWAY=service_port_ip_gateway,
                                       SERVICE_PORT_SUBNET=service_port_subnet,
                                       WLAN_G6_INTERFACE=wlan_g6_interface,
                                       WLAN_G6_SUBNET=wlan_g6_subnet,
                                       WLAN_G7_INTERFACE=wlan_g7_interface,
                                       WLAN_G7_SUBNET=wlan_g7_subnet,
                                       WLAN_G8_STAGING_INTERFACE=wlan_g8_staging_interface,
                                       WLAN_G8_STAGING_SUBNET=wlan_g8_staging_subnet,
                                       WLAN_G8_STAGING_GATEWAY=wlan_g8_staging_gateway,
                                       WLAN_G8_INTERFACE=wlan_g8_interface,
                                       WLAN_G8_SUBNET=wlan_g8_subnet,
                                       CORP_GUEST=corp_guest,
                                       CORP_GUEST_SUBNET=corp_guest_subnet,
                                       REDUNDANCY_IP_PRIMARY=redundancy_ip_primary,
                                       REDUNDANCY_IP_HA_UNIT=redundancy_ip_ha_unit,
                                       DHCP_IP=dhcp_ip,
                                       WLC_NAME=wlc_name,
                                       VTP_DOMAIN=vtp_domain,
                                       SNMP_LOCATION=snmp_location,
                                       RF_NETWORK=rf_network,
                                       G7_RE=g7_re,
                                       AP_COUNTRY=ap_country,
                                       DEFAULT_MANAGEMENT_VLAN=default_management_vlan)
        writefile.write(str(jinja_output))


if __name__ == "__main__":
    xw.Book("Main_Template.xlsm").set_mock_caller()
    main()
