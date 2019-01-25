#coding:utf-8
import math
import random
import datetime

def is_prime(num):
    #Returns True if the number is prime else False
    try_list = []
    pgcd_list = []
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            try_list.append(False)
            pgcd_list.append(x)
        else:
            try_list.append(True)
    if False in try_list:
        print(pgcd_list)
        return False
    else:
        return True

def is_prime_with(num1, num2):
    pass


def generate_number():
    i_m_prime = False
    while i_m_prime is False:
        #num = random.randrange(1000, 9999)
        num = 3457
        i_m_prime = is_prime(num)
    print(num)

def keys():
    p = generate_number()
    q = generate_number()
    n = p * q
    m = (p-1)*(q-1)
    print(m)
def writer(adress):
    pass

def reader(adress):
    pass

def encrypt(public_key):
    pass

def decrypt(private_key):
    pass

start = datetime.datetime.now()
print(generate_number())
print(f"nombre trouvé en {datetime.datetime.now() - start}s")