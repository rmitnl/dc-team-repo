from vars import *
from netmiko import ConnectHandler

# run the show command
network = ConnectHandler(device_type='brocade_fastiron_telnet',ip="192.168.123.12",username=var_u,password=var_p,secret=var_s)
output = network.send_command("show mac-address")
#print(output)
for macs in output.splitlines():
    tokens = macs.split()
    if len(tokens) > 0:
        if tokens[0] not in ["MAC-Address","Total"]:
            print(tokens[0],tokens[1],tokens[4])
print('--------------------------------')
print('Version 2.0')
print('--------------------------------')
network.disconnect()
