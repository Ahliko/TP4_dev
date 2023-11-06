import logging
import socket
from psutil import net_if_addrs

host = net_if_addrs()[[i for i in net_if_addrs()][1]][0][1]
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Données reçues du client : {data.decode()}")
        conn.sendall("Hi mate !".encode())
    except socket.error:
        conn.close()
        logging.critical(f"Connection")
        exit(1)
conn.close()
