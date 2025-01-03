from akips import AKIPS, exceptions
import json
from pprint import pp
from jinja2 import Environment, FileSystemLoader

test1 = AKIPS('qhakips01x.tiretech2.contiwan.com',
              username='api-ro', password='N0Hug54u', verify=False)


def Jinja_Template(hostname_ip: str, hostname_os: str, hostname_location, location_site: str,  type_of_device: str) -> str:
    template_location = r'C:\Users\uie34719\OneDrive - Continental AG\Documents\CONTINENTAL FILES\PERSONAL FILES\REVIEWER-1\DEVNET\OTHERS\PROJECT\SHOWOFF\template'
    env = Environment(loader=FileSystemLoader(template_location), trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('AKIPS_Jinja_Template_HTML.j2')
    jinja_output = template.render(HOSTNAME_IP=hostname_ip,
                                   HOSTNAME_OS=hostname_os,
                                   HOSTNAME_LOCATION=hostname_location,
                                   LOCATION_SITE=location_site,
                                   TYPE_OF_DEVICE=type_of_device)
    return jinja_output


def main():
    with open("AKIPS_MODULE_API_1.html", 'w') as writefile:
        devices = test1.get_devices(group_filter='any', groups=['Cisco'])
        get_group_membership = test1.get_group_membership()
        brackets1 = {}
        for x_key, x_value in devices.items():
            brackets1[x_key] = x_value
        x1 = brackets1
        for x_key1, x_value1 in x1.items():
            hostname_ip = "{{'{}': '{}'}}".format(x_key1, x_value1['ip4addr'])
            hostname_os = x_value1['SNMPv2-MIB.sysDescr']
            hostname_location = x_value1['SNMPv2-MIB.sysLocation']
            location_site = get_group_membership[str(x_key1)][0]
            type_of_device = get_group_membership[str(x_key1)][1]
            x2 = Jinja_Template(hostname_ip, hostname_os, hostname_location, location_site, type_of_device)
            writefile.write(str(x2))


if __name__ == "__main__":
    main()
