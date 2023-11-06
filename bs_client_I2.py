import logging
import socket
from sys import exit

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except socket.error:
    logging.critical("Erreur de connexion !")
    exit(1)

print(f"Connecté avec succès au serveur {host} sur le port {port}")

try:
    msg = str(input("Que veux-tu envoyer au serveur : ")).encode()
except TypeError:
    logging.critical("Erreur de saisie !")
    exit(1)

s.sendall(msg)
data = s.recv(1024)

s.close()
if data is not None:
    print(f"Le serveur a répondu {data.decode()}")
else:
    print("Pas de réponse du serveur !")

exit(0)
