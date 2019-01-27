#coding:utf-8
import datetime
from rsa_m import *
from rsa_v import App

complexity = 2

App()
"""
start = datetime.datetime.now()

m, n, c = calculate_public_key()
u = calculate_private_key(c, m)
public_key = n, c
private_key = u, n
print(f"clef publique: N={public_key[0]} C={public_key[1]}")
print(f"clef privée: U={private_key[0]} N={private_key[1]}")

#print(encrypt("coucou", 2255, 7))
#print(decrypt([1694, 716, 1898, 1694, 716, 1898], 1543, 2255))
print(f"nombre trouvé en {datetime.datetime.now() - start}s")
"""