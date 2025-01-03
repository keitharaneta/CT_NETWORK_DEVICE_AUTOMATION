from akips import AKIPS, exceptions
import json
from pprint import pp

test1 = AKIPS('qhakips01x.tiretech2.contiwan.com',
              username='api-ro', password='N0Hug54u', verify=False)


with open("AKIPS_MODULE_API_1.txt", 'w') as writefile:
    devices = test1.get_devices(group_filter='any', groups=['8-AsiaPac-Switches'])
    x1 = json.dumps(devices, indent=2)
    writefile.write(x1)



#for name, fields in devices.items():
#    print("Device: {} {}".format(name, fields))
