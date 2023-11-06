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

Ce qu'on ~~voudrait~~ veut :

➜ **des logs serveur**

- dans la console
- dans un fichier de log

➜ **des logs client**

- PAS dans la console : c'est le client, c'est un moldu, on lui montre R
- dans un fichier de log

---

Chaque ligne de log :

- **doit être *timestamped***
  - préfixée par date et heure, dans un format standard si possible
- **doit être nivelée**
  - je viens d'inventer le terme
  - c'est à dire que vous préciser un niveau de logging

Il existe des standards sur les niveaux de log en informatique. Les trois en gras sont les plus utilisés. En haut le plus critique, en bas, le moins :

- Emergency
- Alert
- Critical
- **Error** : ERROR ou ERR en rouge
- **Warning** : WARNING ou WARN en jaune
- Notice
- **Informational** : INFO en blanc
- Debug

**Toutes les lignes de log de ce TP devront être au format suivant :**

```
yyyy-mm-dd hh:mm:ss LEVEL message
```

Par exemple :

```
2023-11-03 03:43:21 INFO Un client vient de se co et son IP c'est <CLIENT_IP>.
```

### A. Logs serveur

Le serveur va log chacune des actions à la fois dans la console, et aussi dans un fichier.

Ce fichier il est pas à n'importe quel endroit si on utilise un système GNU/Linux, un dossier est dédié aux logs : `/var/log/`.  
On peut donc créer là-bas un sous-dossier pour notre application, et on stocke dedans le fichier de log de notre application.

Vous pouvez faire ça à la main, ou utiliser [**la librairie `logger`**](https://realpython.com/python-logging/), vous êtes libres pour le moment ! (`logger` c'est le feu quand même).

🌞 **`bs_server_II2A.py`**

- ce qui doit générer une ligne de log :
  - `INFO` lancement du serveur
    - `Le serveur tourne sur <IP>:<port>`
  - `INFO` connexion d'un client
    - l'IP du client doit apparaître dans la ligne de log
    - `Un client <IP_CLIENT> s'est connecté.`
  - `INFO` message reçu d'un client
    - `Le client <IP_CLIENT> a envoyé <MESSAGE>.`
  - `INFO` message envoyé par le serveur
    - `Réponse envoyée au client <IP_CLIENT> : <MESSAGE>.`
  - `WARN` aucun client connecté depuis + de 1 minute
    - le message : `Aucun client depuis plus de une minute.`
    - il doit apparaître toutes les minutes si personne ne se co
- en console
  - le mot-clé `INFO` doit apparaître en blanc
  - le mot clé `WARN` doit apparaître en jaune
- dans un fichier
  - le fichier doit être `/var/log/bs_server/bs_server.log`
  - le créer en amont si nécessaire, précisez la(les) commande(s) dans le compte-rendu

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