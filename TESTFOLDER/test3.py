from akips import AKIPS, exceptions
from json import load, loads, dumps
from pprint import pp


with open('Test123.txt', 'w') as writefile:
    test1 = AKIPS('qhakips01x.tiretech2.contiwan.com',
                  username='api-ro', password='N0Hug54u', verify=False)
    devices = test1.get_device('CTB8-PLCf01')
    x1 = dumps(devices, indent=2)
    writefile.write(str(x1))
