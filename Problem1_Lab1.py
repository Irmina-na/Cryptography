# -*- coding: utf-8 -*-
"""
Nieznane: a - multiplier, c - increment, modulus
"""


import functools

# Linear congruential geneator
def lcg (n, x0, a, c, m):
    tab = [];
    xn = x0;
   
    for i in range (n):
        xn = (a*xn + c) % m;
        tab.append (xn);
    return tab;


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

#Modular inverse
def modinv(b, n):
    g, x, y = egcd(b, n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % n

#Euclidean Algorythm
def GCD(a, b): 
   while(b): 
       a, b = b, a % b 
   return a    
 
    

def conditions(modulus, multiplier, increment, states):
    if modulus < 0:
        raise Exception('condition 1st (modulus>0) unfulfilled = random string')
    elif (modulus < multiplier) or (multiplier < 0):
        raise Exception('condition 2nd (modulus > multiplier > 0) unfulfilled = random string')
    elif (modulus < increment) or (increment <= 0):
        raise Exception('condition 3th (modulus > increment >= 0) unfulfilled = random string')   
    elif (modulus < states[0]) or (states[0] <= 0):
        raise Exception('condition 4th (modulus > x0 >= 0) unfulfilled = random string')
    else:
        print("modulus:", modulus)
        print("multiplier:", multiplier)
        print("increment:", increment)
        return modulus, multiplier, increment 


def unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return conditions(modulus, multiplier, increment, states)
    
def unknown_multiplier(states, modulus):
    print(states[0])
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return unknown_increment(states, modulus, multiplier)

def unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(functools.reduce(GCD, zeroes))
    return unknown_multiplier(states, modulus)

values = unknown_modulus(states =[3, 4, 1, 0, 3, 4])
#values = unknown_modulus(states =[1, 6, 7, 4, 5, 2, 3, 0])

num = lcg (n=1000, x0=0, a=values[1], c=values[2], m=values[0])
print(num[0:7])
print("next number:", num[7])




















