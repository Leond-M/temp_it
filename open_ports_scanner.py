
import re
import socket
import os


def open_ports_scanner() -> None:
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


        #asks for the name of the output file
        file = input("\nPlease type the output file name, or type q or hit enter to exit: ")
        if file == "" or file == "q":
            break
        
        file_path = os.path.join(os.path.dirname(__file__), file)


        #stars port scanning
        with open(file_path, "a") as f:
            open_ports = []
            closed_ports = []

            for port in range(port_min, port_max + 1):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)
                        s.connect((ip, port))
                        open_ports.append(port)
                        print(f"Port {port}:{socket.getservbyport(port)} - Status: OPEN")
                        f.write(f"Port {port}:{socket.getservbyport(port)} - Status: OPEN\n")

                except:
                    closed_ports.append(port)
                    print(f"Port {port} - Status: CLOSED or FILTERED.")
                    f.write(f"Port {port} - Status: CLOSED or FILTERED.\n")
            
            print(f"\n{len(open_ports)} ports are OPEN")
            print(f"{len(closed_ports)} ports are CLOSED or FILTERED")
        
        break


                    
    print("\nGoing back to main menu.\n")

