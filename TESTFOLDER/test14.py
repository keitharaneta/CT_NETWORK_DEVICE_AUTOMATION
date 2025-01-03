from netmiko import ConnectHandler
import json

sw_01 = {
    "device_type": "cisco_ios",
    "host": "10.61.184.5",
    "username": "karaneta",
    "password": "ZRRC3te60!@#",
    "secret": 'ZRRC3te60!@#'
}

connection = ConnectHandler(**sw_01)

output = connection.send_command('show interfaces status', use_textfsm=True)

connection.disconnect()

print(type(output))