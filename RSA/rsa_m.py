# coding:utf-8
import math
import random
import arith_lib

complexity = 2


def is_prime(num):
    # Returns True if the number is prime
    # else return False and a list of denominator
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
        return False, pgcd_list
    else:
        return True


def generate_number():
    # generate a prime number
    # (requires is_prime function)
    i_m_prime = False
    while i_m_prime is False:
        num = random.randrange(int("1"+("0"*(complexity-1))), int("9"*complexity))
        i_m_prime = is_prime(num)
    return num


def calculate_public_key():
    # generate a public key as a tuple and also a variable "m"
    # "m" is useful to calculate private key
    # regarding security reasons, "m" will never be shown to user
    # (requires generate_number and is_prime functions)

    p = generate_number()
    q = generate_number()

    #p = 53
    #q = 97
    n = p * q
    m = (p-1)*(q-1)
    PGCD = 0
    c = 2
    while PGCD != 1:
        c +=1
        (u, v, PGCD) = arith_lib.bezout(c, m)
        
    return m, n, c


def calculate_private_key(c, m):
    (u, v, PGCD) = arith_lib.bezout(c, m)
    if u < 2 or u > m:
        new_u = 1
        k = 1
        while new_u < 2 or new_u > m:
            new_u = u-k*m
            k -= 1
        u = new_u
    return u


def encrypt(string, n, c):
    my_list = [ord(charac) for charac in string]
    my_list2 = []
    for i in my_list:
        my_list2.append((i**c) % n)
    return my_list2


def decrypt(encrypted, u, n):
    my_list = []
    for i in encrypted:
        my_list.append((i**u) % n)
    return ''.join(chr(i) for i in my_list)


def writer(adress):
    pass


def reader(adress):
    pass

def print_something():
    return "i work !!"