from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
print(nr.inventory.hosts)


def get_current_banner(task: Task) -> Result:
    if 1 == int:
        output = task.run(netmiko_send_command, command_string='show inventory')
        return Result(host=task.host, result=output)


output = nr.run(task=get_current_banner)
print_result(output)
