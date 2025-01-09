import sys
from vars import *
from netmiko import ConnectHandler

# check for 2 args
if len(sys.argv) != 3:
    print('2 args required')
    sys.exit(1)

#check for correct args
device = sys.argv[1]
if device[0:8] != "--device":
    print('No device ip')
    sys.exit(1)

output = sys.argv[2]
if output[0:8] != "--output":
    print('No output filter specified')
    sys.exit(1)

# extract data from args 
device = device[9:]
device = device.strip('\"')
output = output[9:]
output = output.strip('\"')

if device not in ["192.168.123.12", "192.168.123.13"]:
    print('Invalid device ip - not in list.')
    sys.exit(1)

if output not in ["up", "down", "all"]:
    print('Output filter type is unknown.')
    sys.exit(1)

# run the show command
print('Version 1.0')
network = ConnectHandler(device_type='brocade_fastiron',ip=device,username=var_u,password=var_p,secret=var_s)
rtrout = network.send_command("show int brief ")

if output == "all":
    print(rtrout)

if output == "up":
    for line in rtrout.splitlines():
        if "Up" in line[0:13]:
            print(line)

if output == "down":
    for line in rtrout.splitlines():
        if "Down" in line[0:13]:
            print(line)

network.disconnect()
