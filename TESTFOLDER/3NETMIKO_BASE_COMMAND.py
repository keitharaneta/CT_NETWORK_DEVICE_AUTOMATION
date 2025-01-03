from time import perf_counter
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from jinja2 import Environment, FileSystemLoader
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


test1 = [{'CTZGx01': '10.223.106.1'}]
test2 = {'CTZGx01': '10.223.106.1'}


def main(x1):
    with open("2TESTING.txt", "w") as writefile:
        for host, ip in x1.items():
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
            send_command_response = conn.send_command("show run | inc ntp")
#            conn.disconnect()
#            print(DEVICE_NETMIKO)
#            print(send_command_response)
            writefile.write(str(send_command_response))
            return send_command_response


print(main(test2))