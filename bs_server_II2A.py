import logging
import threading
import time

import colorlog
import socket
from psutil import net_if_addrs
import argparse

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/bs_server.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'white',
        'WARN': 'yellow',
        'WARNING': 'orange',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

argparser = argparse.ArgumentParser(description="Serveur de chat.")
argparser.add_argument("-p", "--port", type=int, help="Port d'écoute du serveur")
argv = argparser.parse_args()


def check_connections():
    last_check = time.time()
    while True:
        if time.time() - last_check >= 60:
            logging.warn('Aucun client ne s\'est connecté depuis la dernière minute.')
            last_check = time.time()


check_thread = threading.Thread(target=check_connections)

if argv.port is None:
    logger.warning("Le port n'a pas été spécifié, le port par défaut (13337) sera utilisé.")
    port = 13337
else:
    if int(argv.port) <= 0 or int(argv.port) >= 65535:
        logger.error("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        exit(1)
    if int(argv.port) <= 1024:
        logger.error("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")

        exit(2)
    port = int(argv.port)

host = net_if_addrs()[[i for i in net_if_addrs()][2]][0][1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
logger.info(f"Le serveur tourne sur {host}:{port}")
check_thread.start()
conn, addr = s.accept()
logger.info(f"Un client {addr} s'est connecté.")
check_thread.join()
while True:
    try:
        data = conn.recv(1024)
        if not data:
            logger.warning("Le client n'a pas envoyé de données.")
            break
        logger.info(f"Le client {addr} a envoyé {data.decode()}.")
        if data.decode().__contains__("meo"):
            logger.info(f"Réponse envoyée au client {addr} : Meo à toi confrère.")
            conn.sendall("Meo à toi confrère.".encode())
        elif data.decode().__contains__("waf"):
            logger.info(f"Réponse envoyée au client {addr} : ptdr t ki.")
            conn.sendall("ptdr t ki".encode())
        else:
            conn.sendall("Mes respects humble humain.".encode())
            logger.info(f"Réponse envoyée au client {addr} : Mes respects humble humain.")

    except socket.error:
        conn.close()
        logging.error(f"Problème de connexion")
        exit(1)
conn.close()
