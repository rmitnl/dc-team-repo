from netmiko import Netmiko
import argparse

devices = [{
    "device_type": "cisco_xr",
    "ip": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "22",
}]

parser = argparse.ArgumentParser()
parser.add_argument("--cmd", type=str)
args = parser.parse_args()

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command(args.cmd)
    net_connect.disconnect()
    print ("Cmd: " + args.cmd + "\n" + output)
