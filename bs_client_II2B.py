import logging
import colorlog
import re
import socket
from sys import exit

host = '10.1.1.11'
port = 13337

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/bs_client/bs_client.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.ERROR)
formatter_file = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
formatter_stream = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)

file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_stream)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    logger.error(f"Impossible de se connecter au serveur {host} sur le port {port}.")
    exit(1)

logger.info(f"Connexion réussie à {host}:{port}.")

try:
    msg = input("Que veux-tu envoyer au serveur : ")
    if type(msg) is not str:
        raise TypeError
    if re.findall(r'\b(meo|waf)\b', msg) is None:
        raise "NoneException"
except "NoneException":
    logging.error("Erreur ! Le message doit contenir soit 'meo' soit 'waf' !")
    exit(1)
except TypeError:
    logging.error("Erreur ! Le message doit être une chaîne de caractères !")
    exit(1)

s.sendall(msg.encode())
logger.info(f"Message envoyé au serveur {host} : {msg}.")
data = s.recv(1024)
logger.info(f"Réponse reçue du serveur {host} : {data.decode()}.")

s.close()
if data is not None:
    print(f"Le serveur a répondu {data.decode()}")
else:
    print("Pas de réponse du serveur !")

exit(0)
