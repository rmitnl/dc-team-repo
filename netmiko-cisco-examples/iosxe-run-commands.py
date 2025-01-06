from netmiko import Netmiko
import argparse
import json

def run_commands(commands):
    device = {
            "device_type": "cisco_xe",
            "ip": "devnetsandboxiosxe.cisco.com",
            "username": "admin",
            "password": "C1sco12345",
            "port": "22",
        }
    for command in commands:
        # Replace this with the logic to execute each command
        #print(f"Executing command: {command}")
        net_connect = Netmiko(**device)
        output = net_connect.send_command(command)
        net_connect.disconnect()
        print (output)
        # Example: send the command to the device or system

def main():
    parser = argparse.ArgumentParser(description="Run multiple IOS XE commands with individual flags.")
    
    # Allow multiple occurrences of the --command flag
    parser.add_argument(
        '-c', '--commands',
        nargs='+',
        #action='append', 
        required=True, 
        help="Specify a command to execute. Use multiple -c flags for multiple commands."
    )
    args = parser.parse_args()

    # Pass the list of commands to the execution function
    run_commands(json.loads(args.commands[0]))

if __name__ == "__main__":
    main()
