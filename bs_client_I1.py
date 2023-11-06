import socket

host = '10.1.1.11'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall('Meooooo !'.encode())
data = s.recv(1024)

s.close()
if data is not None:
    print(f"Le serveur a répondu {data.decode()}")
else:
    print("Pas de réponse du serveur !")
