import sys
from vars import *
from netmiko import ConnectHandler

# check for 1 arg
if len(sys.argv) != 2:
    print('1 arg required (description)')
    sys.exit(1)

# verify arg(s)
name = sys.argv[1]
if name[0:6] != "--name":
    print('name not set')
    sys.exit(1)

# extract data from arg(s)
name = name[7:]
name = name.strip('\"')
name = name.replace(" ", "_")

# run the commands
device = {
    "device_type": "brocade_fastiron",
    "host": "192.168.123.12",
    "username": var_u,
    "password": var_p,
    "secret": var_s
}
port_name_cmd = "port-name " + name
commands = ["interface ethernet 1/1/1",port_name_cmd]
with ConnectHandler(**device) as net_connect:
    print('\n-> Previous config:')
    output = net_connect.send_config_set(commands)
    output = net_connect.send_command("show config | begin ethernet 1/1/1")
    count=0
    for line in output.splitlines():
        print(line)
        count +=1
        if count >= 4:
            break
    output += net_connect.save_config()
    print('\n-> Current config:')
    output = net_connect.send_command("show config | begin ethernet 1/1/1")
    count=0
    for line in output.splitlines():
        print(line)
        count +=1
        if count >= 4:
            break
