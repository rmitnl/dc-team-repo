import sys, time
from vars import *
from netmiko import ConnectHandler

# check for 3 arg
if len(sys.argv) != 4:
    print('3 args required (host, interface, name)')
    sys.exit(1)

# verify arg(s)
host = sys.argv[1]
if host[0:6] != "--host":
    print('host not set')
    sys.exit(1)

interface = sys.argv[2]
if interface[0:11] != "--interface":
    print('interface not set')
    sys.exit(1)

name = sys.argv[3]
if name[0:6] != "--name":
    print('name not set')
    sys.exit(1)

# extract data from arg(s)
host = host[7:]
interface = interface[12:]
name = name[7:]
name = name.strip('\"')
name = name.replace(" ", "_")

# run the commands
device = {
    "device_type": "brocade_fastiron",
    "host": host,
    "username": var_u,
    "password": var_p,
    "secret": var_s
}
port_name_cmd = "port-name "+name
commands = ["interface "+interface, port_name_cmd]
with ConnectHandler(**device) as net_connect:
    print('\n-> Previous config:')
    output = net_connect.send_command("show config | begin "+interface)
    count=0
    for line in output.splitlines():
        print(line)
        count +=1
        if count >= 4:
            break
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()
    time.sleep(2)
    print('\n-> Current config:')
    output = net_connect.send_command("show config | begin "+interface)
    count=0
    for line in output.splitlines():
        print(line)
        count +=1
        if count >= 4:
            break
