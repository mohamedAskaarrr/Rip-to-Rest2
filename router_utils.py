from netmiko import ConnectHandler
from typing import Dict, List

class RouterConnection:
    def __init__(self, router_ip: str, username: str = "", password: str = "cisco"):
        self.device = {
            "device_type": "cisco_ios_telnet",  # Using Telnet for Packet Tracer
            "host": router_ip,
            "username": "",  # Usually empty for Packet Tracer basic setups
            "password": "cisco",
        }

    def get_rip_routes(self) -> List[Dict]:
        """Get RIP routes from the router"""
        try:
            with ConnectHandler(**self.device) as net_connect:
                output = net_connect.send_command("show ip route rip", use_textfsm=True)
                return output if output else []
        except Exception as e:
            print(f"Error connecting to router: {str(e)}")
            return []

    def get_rip_neighbors(self) -> List[Dict]:
        """Get RIP neighbors from the router"""
        try:
            with ConnectHandler(**self.device) as net_connect:
                output = net_connect.send_command("show ip protocols | section Routing Protocol is rip", use_textfsm=True)
                return output if output else []
        except Exception as e:
            print(f"Error connecting to router: {str(e)}")
            return []

# Define your router IPs from Packet Tracer simulation
ROUTER_IPS = [
    "192.168.1.1",
    "192.168.3.1"
    # Add more router IPs as needed
] 