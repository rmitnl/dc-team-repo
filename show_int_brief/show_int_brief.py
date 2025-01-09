import sys
from vars import *
from netmiko import ConnectHandler

# run the show command
print('--------------------------------')
print('Version 1.0')
print('--------------------------------')
network = ConnectHandler(device_type='brocade_fastiron',ip="192.168.123.12",username=var_u,password=var_p,secret=var_s)
output = network.send_command("show interface brief")

# show output
print(output)
network.disconnect()
