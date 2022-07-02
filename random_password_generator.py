# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 22:25:14 2022

@author: Anujan
"""

import random as random

user = int(input(f"please enter length of password \n"))
keys = [chr(n) for n in range(97, 123)] + [chr(n) for n in range(65, 91)] + [chr(n) for n in range(48, 58)] + [chr(n) for n in range(33, 39)]
password = []

for i in range(0, user):
    ind = random.randint(0, len(keys))
    password+=keys[ind]
    
print("".join(password))