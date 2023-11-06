import logging
import socket
from psutil import net_if_addrs

host = net_if_addrs()[[i for i in net_if_addrs()][2]][0][1]
print(host)
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr}.")
while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        elif data.decode().__contains__("meo"):
            conn.sendall("Meo à toi confrère.".encode())
        elif data.decode().__contains__("waf"):
            conn.sendall("ptdr t ki".encode())
        else:
            conn.sendall("Mes respects humble humain.".encode())

    except socket.error:
        conn.close()
        logging.critical(f"Problème de connexion")
        exit(1)
conn.close()
