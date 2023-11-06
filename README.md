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

[bs_client_I2.py](bs_client_I2.py)

🌞 **`bs_server_I2.py`**

[bs_server_I2.py](bs_server_I2.py)

## 3. You say client I hear control


🌞 **`bs_client_I3.py`**

[bs_client_I3.py](bs_client_I3.py)