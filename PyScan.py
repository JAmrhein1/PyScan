import socket
import threading
import subprocess
import platform
from termcolor import colored
from port_service_map import port_service_map

banner_text = """\033[1m
 ______        ______                   
(_____ \      / _____)                  
 _____) )   _( (____   ____ _____ ____  
|  ____/ | | |\____ \ / ___|____ |  _ \ 
| |    | |_| |_____) | (___/ ___ | | | |
|_|     \__  (______/ \____)_____|_| |_|
       (____/                           \033[0m
"""
colored_banner = colored(banner_text, 'red')
print(colored_banner)
print(colored("\033[1m[!] Warning This network scanning tool is intended for educational purposes only. Unauthorized scanning of networks or systems is illegal and may result in severe legal consequences. Ensure that you have explicit permission from the network owner before using this tool. Use at your own risk. [!]\033[0m", "magenta"))
print(" ")
print(colored("\033[1m[!] The developer is not responsible for any damage caused by this tool. [!]\033[0m", "magenta"))
print(" ")

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    if ':' in ip:  # IPv6
        command = ['ping', '-6', param, '1', ip] if platform.system().lower() == 'windows' else ['ping6', param, '1', ip]
    else:  # IPv4
        command = ['ping', param, '1', ip]
    try:
        if subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            return True
    except FileNotFoundError:
        print("Ping command not found. Please ensure ping is installed and available in your PATH.")
    return False

def grab_banner(ip, port):
    try:
        family = socket.AF_INET6 if ':' in ip else socket.AF_INET
        sock = socket.socket(family)
        sock.connect((ip, port))
        sock.settimeout(2)
        banner = sock.recv(1024).decode().strip()
        return banner
    except Exception:
        return None

def scan_port(ip, port, show_only_open, open_ports):
    try:
        family = socket.AF_INET6 if ':' in ip else socket.AF_INET
        sock = socket.socket(family, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            banner = grab_banner(ip, port)
            port_output = f"\033[1;35mPort {port}\033[0m"  # Magenta and bold
            service_name = port_service_map.get(port, 'Unknown')
            if banner:
                open_ports.append((port, banner, service_name))
                if show_only_open:
                    print(f"{port_output} is open on {ip} (Service: {service_name}, Banner: {banner})")
            else:
                open_ports.append((port, None, service_name))
                if show_only_open:
                    print(f"{port_output} is open on {ip} (Service: {service_name})")
        elif not show_only_open:
            print(f"Port {port} is closed on {ip}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port} on {ip}: {e}")

def scan_ports(ip, start_port, end_port, ignored_ports, show_only_open):
    threads = []
    open_ports = []

    for port in range(start_port, end_port + 1):
        if port not in ignored_ports:
            thread = threading.Thread(target=scan_port, args=(ip, port, show_only_open, open_ports))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
    
    return open_ports

def main():
    while True:
        target = input("Enter the target IP address (IPv4 or IPv6) or domain: ")
        
        try:
            target_ip = socket.getaddrinfo(target, None)[0][4][0]
        except socket.gaierror:
            print(f"Invalid target: {target}")
            return
        
        if not ping_host(target_ip):
            print(f"Host {target_ip} is not reachable.")
            return
        
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        
        ignored_ports_input = input("Enter ports to ignore (comma-separated, e.g., 22,80,443): ")
        ignored_ports = list(map(int, ignored_ports_input.split(','))) if ignored_ports_input else []
        
        show_only_open = input("Show only open ports? (yes/no): ").strip().lower() == 'yes'
        
        open_ports = scan_ports(target_ip, start_port, end_port, ignored_ports, show_only_open)

        if not show_only_open:
            print("\nOpen ports:")
            for port, banner, service_name in open_ports:
                port_output = f"\033[1;35mPort {port}\033[0m"  # Magenta and bold
                if banner:
                    print(f"{port_output} is open on {target_ip} (Service: {service_name}, Banner: {banner})")
                else:
                    print(f"{port_output} is open on {target_ip} (Service: {service_name})")

        print("\nThe scan is complete. See above for the open ports.")
        
        scan_again = input("Would you like to scan another network? (yes/no): ").strip().lower()
        if scan_again != 'yes':
            print(colored("\033[1mThank you for using PyScan!\033[0m", "magenta"))
            break

if __name__ == "__main__":
    main()