# TP4 : I'm Socketing, r u soketin ?

# [I. Simple bs program](#I-Simple-bs-program)

# [II. You say dev I say good practices](#ii-You-say-dev-I-say-good-practices)

# [III. COMPUTE](#iii-compute)

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

## 1. Args

🌞 **`bs_server_II1.py`**

[bs_server_II1.py](bs_server_II1.py)

```bash
$ python bs_server_II1.py -p 8888
```

## 2. Logs

### A. Logs serveur

🌞 **`bs_server_II2A.py`**


```bash
sudo pip install colorlog
sudo mkdir /var/log/bs_server -m 700 && sudo chown -R $(whoami):$(whoami) /var/log/bs_server && touch /var/log/bs_server/bs_server.log && chmod 600 /var/log/bs_server/bs_server.log
```

```bash
python bs_server_II2A.py -p 8888
```

[bs_server_II2A.py](bs_server_II2A.py)

### B. Logs client

🌞 **`bs_client_II2B.py`**


```bash
sudo mkdir /var/log/bs_client -m 700 && sudo chown -R $(whoami):$(whoami) /var/log/bs_client && touch /var/log/bs_client/bs_client.log && chmod 600 /var/log/bs_client/bs_client.log
```
```bash
python bs_client_II2B.py
```

[bs_client_II2B.py](bs_client_II2B.py)

# III. COMPUTE

🌞 **`bs_client_III.py`**

```bash
sudo mkdir /var/log/bs_client -m 700 && sudo chown -R $(whoami):$(whoami) /var/log/bs_client && touch /var/log/bs_client/bs_client.log && chmod 600 /var/log/bs_client/bs_client.log
```
```bash
python bs_client_III.py
```

[bs_client_III.py](bs_client_III.py)

🌞 **`bs_server_III.py`**

```bash
sudo mkdir /var/log/bs_server -m 700 && sudo chown -R $(whoami):$(whoami) /var/log/bs_server && touch /var/log/bs_server/bs_server.log && chmod 600 /var/log/bs_server/bs_server.log
```

```bash
python bs_server_III.py
```

[bs_server_III.py](bs_server_III.py)