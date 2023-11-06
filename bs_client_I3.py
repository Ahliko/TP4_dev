import logging
import re
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
    msg = input("Que veux-tu envoyer au serveur : ")
    if type(msg) is not str:
        raise TypeError
    if re.findall(r'\b(meo|waf)\b', msg) is None:
        raise "NoneException"
except "NoneException":
    logging.critical("Erreur ! Le message doit contenir soit 'meo' soit 'waf' !")
    exit(1)
except TypeError:
    logging.critical("Erreur ! Le message doit être une chaîne de caractères !")
    exit(1)

s.sendall(msg)
data = s.recv(1024)

s.close()
if data is not None:
    print(f"Le serveur a répondu {data.decode()}")
else:
    print("Pas de réponse du serveur !")

exit(0)
