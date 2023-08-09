import socket
import ipaddress
import threading
import concurrent.futures

def scan_host(ip):
    try:
        host_name = socket.gethostbyaddr(str(ip))[0]
        print(f"IP: {ip} - Hostname: {host_name}")
    except socket.herror:
        print(f"IP: {ip} - No Hostname")

def main():
    print("Scanning devices in the local network...\n")
    
    local_ip = socket.gethostbyname(socket.gethostname())
    network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(scan_host, ip) for ip in network.hosts()]
    
    print("\nScanning completed.")

if __name__ == "__main__":
    main()
