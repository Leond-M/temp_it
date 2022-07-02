
from windows_updates import scan_for_windows_updates
from open_ports_scanner import open_ports_scanner
from vulnerable_banner_scanner import banner_scanner

PORT_MIN = 0
PORT_MAX = 65535

def main():
    print("\n--------------------------------------------------------------")
    print("\nWelcome to this small vulnerabily scanner.")
    print("\n--------------------------------------------------------------")

    try:

        while True:
            print("\nThis are the options you can choose from:")
            print("\n[1] Scan for updates in the host windows machine.")
            print("[2] Scan for open ports in the target machine.")
            print("[3] Scan for vulnerable banners in the target machine.")
            print("[4] Exit.\n")

            choice = input("\nPlease choose a number from 1 to 4: ")


            #Sadly, we can  not use python 3.10 in windows 7.
            """#this was introduced in verion 3.10. This will not work in earlier versions of python
            #https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
            match choice:
                case "1":
                    raise Exception("Not implemented")
                case "2":
                    raise Exception("Not implemented")
                case "3":
                    raise Exception("Not implemented")
                case _:
                    print(f"{choice} is not a valid option.") """


            if choice == "1":
                _ = scan_for_windows_updates()
            elif choice == "2":
                open_ports_scanner()
            elif choice == "3":
                banner_scanner()
            elif choice == "4":
                break
            else:
                print(f"\n{choice} is not a valid option.")
                continue

            print("\n JOB DONE.")

        print("\nThe script has finished.")
        
        #exceptions handling
    except Exception as e:
        print(f"Something went wrong, the error is: {e}")



if __name__ == "__main__":
    main()