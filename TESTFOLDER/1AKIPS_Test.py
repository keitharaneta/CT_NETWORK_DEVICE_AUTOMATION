from akips import AKIPS, exceptions
from json import load, loads, dumps
from pprint import pp


with open('Test123.txt', 'w') as writefile:
    test1 = AKIPS('qhakips01x.tiretech2.contiwan.com',
                  username='api-ro', password='N0Hug54u', verify=False)
    devices = test1.get_group_membership()
    x1 = devices['CTLQx02'][0]
    x2 = devices['CTLQx02'][1]
    x3 = 'This {} device type is {}'.format(x1, x2)
    writefile.write(str(x3))
