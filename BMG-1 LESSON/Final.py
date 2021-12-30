# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 21:56:07 2021

@author: Mehmet Emin Ural
"""

import numpy as np

dizi=np.arange(10)
#print(dizi)

matris9=np.random.randint(10,50,size=(3,5))
print(matris9)
print("*"*20)
print(matris9[1:3,1:3])

print("*"*20)
print(matris9[1:,:])
print("*"*25)
matris10=np.arange(1,51)
matris10 = matris10.reshape(5,10)
print(matris10)

print(matris10[1:3,1:3])