import subprocess
import socket
import ipaddress

def is_host_alive(ip):
    # Use ping to check if the host is alive
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

def network_mapper():
    # Get user input for the network IP range
    network_range = input("Enter the network IP range (e.g., '192.168.1.0/24'): ")

    # Validate the input and get the IP addresses within the network range
    try:
        network = ipaddress.IPv4Network(network_range)
        hosts = [str(ip) for ip in network.hosts()]
    except ValueError:
        print("Invalid network IP range. Please enter a valid CIDR notation.")
        return

    # Scan each host in the network range
    print("Scanning for active hosts in the network range...")
    active_hosts = []
    for host in hosts:
        if is_host_alive(host):
            active_hosts.append(host)

    # Print out the list of active hosts
    print("Active hosts in the network range:")
    for host in active_hosts:
        print("Host:", host)

if __name__ == "__main__":
    network_mapper()