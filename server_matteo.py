import argparse
import socket
import logging

import colorlog

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", type=int, default="13337", help="specify the port to connect to")
args = parser.parse_args()

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/var/log/bs_server/bs_server.log', 'w', 'utf-8')
file_handler.setLevel(logging.INFO)
stream_handler = colorlog.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
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
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename='/var/log/bs_server/bs_server.log', encoding='utf-8', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

if (args.port < 0 or args.port > 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif (args.port >= 0 and args.port <= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)

host = ''
port = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
logger.info(f"Le serveur tourne sur {port}.")
s.listen(1)

conn, addr = s.accept()

logger.info(f"Un client {addr[0]} s'est connecté.")

response = "error"

try:
    try:
        while True:
            data = conn.recv(1024)
            if not data: break
            logger.info(f"Le client {addr[0]} a envoyé {data.decode()}.")
            if ("meo" in data.decode()):
                logger.info(f"Le client {addr[0]} a envoyé 'meo'.")
                response = "Meo à toi confrère."
            elif ("waf" in data.decode()):
                logger.info(f"Le client {addr[0]} a envoyé 'waf'.")
                response = "ptdr t ki"
            else:
                logger.info(f"Le client {addr[0]} a envoyé autre chose.")
                response = "Mes respects humble humain."
            logger.info(f"Réponse à envoyer au client {addr[0]} : {response}.")
            conn.sendall(response.encode())
            logger.info(f"Réponse envoyée au client {addr[0]} : {response}.")
    except socket.error:
        print("Erreur de connexion.")
finally:
    conn.close()
    s.close()
