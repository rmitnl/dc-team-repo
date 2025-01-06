from netmiko import Netmiko

devices = [
{
    "device_type": "cisco_xe",
    "ip": "devnetsandboxiosxe.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "22",
}]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show interfaces")
    net_connect.disconnect()
    print (output)
