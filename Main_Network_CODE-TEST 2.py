from time import perf_counter
from netmiko import ConnectHandler
import xlwings as xw
import json

""" <DOC STRING HERE> """
def performance_counter(func):
    def script_tester(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        performance = finish - start
        print(f'Execution Time: {performance}')
    return script_tester


v_hostname_ip = {'CTKLx05': '10.61.184.5', 'CTKLx06': '10.61.184.6', 'CTKLx08': '10.61.184.8'}
v_hostname_ip_single = {'CTKLx05': '10.61.184.5'}
v_hostname_ip_single_change = ["ntp server 10.203.52.20"]


@performance_counter
@xw.func
def main():
#    with open('2NETMIKO_TESTING.txt', 'w') as writefile1:
    for host, ip in v_hostname_ip_single.items():
        DEVICE_NETMIKO = {
            'host': ip,
            'port': 22,
            'username': 'karaneta',
            'password': 'ZRRC3te60!@#',
            'secret': 'ZRRC3te60!@#',
            'device_type': "cisco_ios",
        }
        conn = ConnectHandler(**DEVICE_NETMIKO)
        conn.enable()
        send_command_response = conn.send_config_set(v_hostname_ip_single_change)
        conn.disconnect()
        print(DEVICE_NETMIKO)
        print(send_command_response)
#            writefile1.write(str(send_command_response))


def test1():
    print(f'{main()}')  


if __name__ == "__main__":
     main()
