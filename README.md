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

🌞 **`bs_client_I1.py`**

[bs_client_I1.py](bs_client_I1.py)

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

> Vous aurez besoin du [**cours sur la gestion d'erreurs**](../../../../cours/dev/error_handling/README.md) pour cette partie.

- retour visuel
    - afficher un message de succès chez le client quand il se co au serveur
    - le message doit être : `Connecté avec succès au serveur <IP_SERVER> sur le port <PORT>`
    - vous utiliserez un `try` `except` pour savoir si la connexion est correctement effectuée
- le programme doit permettre à l'utilisateur d'envoyer la string qu'il veut au serveur
    - on peut récupérer un input utilisateur avec la fonction `input()` en Python
    - au lancement du programme, un prompt doit apparaître pour indiquer à l'utilisateur qu'il peut envoyer une string au serveur :
        - `Que veux-tu envoyer au serveur : `

🌞 **`bs_server_I2.py`**

- retour visuel
    - afficher un message de succès quand un client se co
    - le message doit être : `Un client vient de se co et son IP c'est <CLIENT_IP>.`
- réponse adaptative
    - si le message du client contient "meo" quelque part, répondre : `Meo à toi confrère.`
    - si le message du client contient "waf" quelque part, répondre : `ptdr t ki`
    - si le message du client ne contient PAS "meo", ni "waf", répondre : `Mes respects humble humain.`

## 3. You say client I hear control

On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.

🌞 **`bs_client_I3.py`**

- vérifier que...
    - le client saisit bien une string
        - utilisez la méthode native `type()` pour vérifier que c'est une string
    - que la string saisie par le client contient obligatoirement soit "waf" soit "meo"
        - utilisez [**une expression régulière**](https://www.programiz.com/python-programming/regex) (signalez-le moi s'il serait bon de faire un cours sur cette notion)
- sinon lever une erreur avec `raise`
    - choisissez avec pertinence l'erreur à lever dans les deux cas (s'il saisit autre chose qu'une string, ou si ça contient aucun des deux mots)
    - y'a une liste des exceptions natives (choisissez-en une donc) tout en bas du [cours sur la gestion d'erreur](../../../../cours/dev/error_handling/README.md)

> On poussera le contrôle plus loin plus tard.