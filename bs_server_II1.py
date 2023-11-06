import logging
import socket
from psutil import net_if_addrs
import argparse

argparser = argparse.ArgumentParser(description="Serveur de chat.")
argparser.add_argument("-p", "--port", type=int, help="Port d'écoute du serveur")
argv = argparser.parse_args()

if argv.port is None:
    port = 13337
else:
    if int(argv.port) <= 0 or int(argv.port) >= 65535:
        logging.critical("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        exit(1)
    if int(argv.port) <= 1024:
        logging.warning("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
        exit(2)
    port = int(argv.port)

host = net_if_addrs()[[i for i in net_if_addrs()][2]][0][1]
print(host)


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
