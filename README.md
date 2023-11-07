# TP4 : I'm Socketing, r u soketin ?

# [I. Simple bs program](#I. Simple bs program)

# [II. You say dev I say good practices](./2_good_practices/README.md)

# [III. COMPUTE](./3_compute/README.md)

# I. Simple bs program

- [I. Simple bs program](#i-simple-bs-program)
    - [1. First steps](#1-first-steps)
    - [2. User friendly](#2-user-friendly)
    - [3. You say client I hear control](#3-you-say-client-i-hear-control)

## 1. First steps

🌞 **`bs_server_I1.py`**

[bs_server_I1.py](bs_server_I1.py)

```bash
python bs_server_I1.py
```

🌞 **`bs_client_I1.py`**

[bs_client_I1.py](bs_client_I1.py)

```bash
python bs_client_I1.py
```

🌞 **Commandes...**

```bash
[ahliko@tp4 ~]$ sudo dnf install git -y
[ahliko@tp4 ~]$ git clone git@github.com:Ahliko/TP4_dev.git
[ahliko@tp4 ~]$ cd TP4_dev
[ahliko@tp4 TP4_dev]$ sudo dnf install python-pip -y
[ahliko@tp4 TP4_dev]$ sudo pip install psutil
[ahliko@tp4 TP4_dev]$ sudo firewall-cmd --add-port=13337/tcp --permanent
success
[ahliko@tp4 TP4_dev]$ sudo firewall-cmd --reload
success
[ahliko@tp4 ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources: 
  services: cockpit dhcpv6-client ssh
  ports: 13337/tcp
  protocols: 
  forward: yes
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules:
[ahliko@tp4 TP4_dev]$ python3 bs_server_I1.py
[ahliko@tp4 TP4_dev]$ python bs_server_I1.py
10.1.1.11
Connected by ('10.1.1.0', 34426)
Données reçues du client : Meooooo !
[ahliko@tp4 ~]$ sudo ss -alnpt | grep python
LISTEN 0      1          10.1.1.11:13337      0.0.0.0:*    users:(("python",pid=1359,fd=3))
```

## 2. User friendly

🌞 **`bs_client_I2.py`**

[bs_client_I2.py](bs_client_I2.py)

```bash
python bs_client_I2.py
```

🌞 **`bs_server_I2.py`**

[bs_server_I2.py](bs_server_I2.py)

```bash
python bs_server_I2.py
```

## 3. You say client I hear control


🌞 **`bs_client_I3.py`**

[bs_client_I3.py](bs_client_I3.py)

```bash
python bs_client_I3.py
```

# II. You say dev I say good practices

- [II. You say dev I say good practices](#ii-you-say-dev-i-say-good-practices)
  - [1. Args](#1-args)
  - [2. Logs](#2-logs)
    - [A. Logs serveur](#a-logs-serveur)
    - [B. Logs client](#b-logs-client)
    - [C. NOTE IMPORTANTE](#c-note-importante)

## 1. Args

🌞 **`bs_server_II1.py`**

[bs_server_II1.py](bs_server_II1.py)

```bash
$ python bs_server_II1.py -p 8888
```

## 2. Logs

**Allô les dévs ? Ici it4 l'admin qui vous parle. Ils sont où les ptain de logs de votre application bowdel.**

![No logs](../img/nologs.jpg)


### A. Logs serveur

🌞 **`bs_server_II2A.py`**


```bash
sudo mkdir /var/log/bs_server -m 666 && sudo touch /var/log/bs_server/bs_server.log && sudo chmod 666 /var/log/bs_server/bs_server.log
```

```bash
python bs_server_II2A.py -p 8888
```

[bs_server_II2A.py](bs_server_II2A.py)

### B. Logs client

Les logs du client, c'est que dans un fichier. En effet, que ce soit une app console ou graphique, le client on veut lui montrer que ce qui est directement lié à SON utilisation de l'application. Et pas le reste.   
Donc on lui jette pas les logs et des vilaines erreurs au visage, ni 14000 messages informatifs.

Je vous laisse choisir l'emplacement du fichier de log de façon **pertinente**.

🌞 **`bs_client_II2B.py`**

- ce qui doit générer une ligne de log :
  - `INFO` connexion réussie à un serveur
    - `Connexion réussie à <IP>:<PORT>.`
  - `INFO` message envoyé par le client
    - `Message envoyé au serveur <IP_SERVER> : <MESSAGE>.`
  - `INFO` message reçu du serveur
    - `Réponse reçue du serveur <IP_SERVER> : <MESSAGE>.`
  - `ERROR` connexion au serveur échouée
    - pour le tester, il suffit de lancer le client alors que le serveur est éteint !
    - le message : `Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.`
- en console
  - affiche juste `ERROR Impossible de se connecter au serveur <IP_SERVER> sur le port <PORT>.` en rouge quand ça fail (pas de timestamp là)
  - les messages de niveau INFO ne sont pas visibles dans la console du client
- dans un fichier
  - `<DOSSIER_DE_LOG>/bs_client.log`

### C. NOTE IMPORTANTE

**A partir de maintenant, vous savez gérer des logs à peu près proprement.**

Vous allez dév plusieurs machins en cours, vous devrez utiliser exactement la même méthode que précédemment pour générer les logs : timestamp, niveau de log, message, stocké dans un fichier précis etc.