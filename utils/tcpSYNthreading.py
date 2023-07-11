import threading
import socket
from args import *

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f'{port} open')
        sock.close()
    except socket.error:
        pass

def port_scan(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()
        

if __name__ == '__main__':
    host = parse()
    start_port = 1
    end_port = 100
    port_scan(host, start_port, end_port)