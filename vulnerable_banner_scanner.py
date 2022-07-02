import socket
import re
import os

file_path = os.path.join(os.path.dirname(__file__), "banners.txt")

def banner_scanner() -> None:

    while True:
        #ask user for ip
        ip = input("\nPlease enter the ip address that you want to scan, or input q or hit enter to exit: ")

        if ip == "" or ip == "q":
            break

        elif re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
            print(f"{ip} is a valid ip address")

        else:
            print(f"{ip} is not a valid ip address")
            continue
            
        #ask user for the port range
        print("\nPlease enter the range of ports you want to scan in format: xx-xx (example: 80-440), or type q or hit enter to exit: ")
        ports = input("Enter port range: ")

        if ports == "" or ports == "q":
            break

        port_range_regex = re.compile("([0-9]+)-([0-9]+)")
        is_valid = port_range_regex.search(ports.replace(" ", ""))

        if is_valid:
            port_min = int(is_valid.group(1))
            port_max = int(is_valid.group(2))

        else:
            print(f"{ports} is not a valid port range")
            continue

        #stars port scanning, and creates the output file

        total_vulnerable= 0

        print('Scan started. This can take a while...')

        #this list can be improved adding more vulnerabilities from the db.
        #there are more here: https://github.com/offensive-security/exploitdb/tree/master/exploits/linux/remote
        with open(file_path, "r") as r:
            for port in range(port_min, port_max + 1):
                try:
                    
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)
                        s.connect((ip, port))
                        banner = s.recv(1024).decode('utf-8').strip("\r").strip("\n").strip()

                        r.seek(0,0)
                        for line in r.readlines():
                            striped = line.strip('\n').strip("\r").strip()
                            if striped == banner:
                                print(f"Found in port {port} vulnerable banner: {banner}")
                                total_vulnerable += 1
                                break

                except Exception as e:
                    pass

        
        print(f"\nWe found {total_vulnerable} exploitable services.")

        
        break
                    
    print("\nGoing back to main menu.\n")