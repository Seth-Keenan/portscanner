import socket

def port_range(port):
    if (port == 0):
        print("Well Known Ports: ")
    if (port == 1024):
        print("Registered Ports: ")
    if (port == 49152):
        print("Dynamic or Private Ports: ")
    else:
        pass

def port_scan(ip_address):
    for port in range(0,65535):
        port_range(port)

        open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = open_socket.connect_ex((ip_address, port))

        if result == 0:
            print("Port " + str(port) + " is open")
        else:
            pass

        open_socket.close

def main():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    port_scan(ip_address)

main()