#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:56:01 2021

@author: bing
"""

import random
import string



def caesarEncrypt(message, codebook, shift):
    '''
    - you can compute the index of a character, or,
    - you can convert the codebook into a dictionary
    '''
    
    encrypted = ""
    ##put your code here
    max = len(codebook) - 1
    for i in message:
        if i.isalpha():
            location = codebook.index(i)
            new_location = location + shift
            if new_location <= max:
                encrypted += codebook[new_location]
            else:
                encrypted += codebook[new_location - max + 1]
        else:
            encrypted += i
    return encrypted


def caesarDecrypt(message, codebook, shift):
    decrypted = ""
    ##put your code here
    max = len(codebook)
    for i in message:
        if i.isalpha():
            location = codebook.index(i)
            new_location = location - shift
            if new_location >= 0:
                decrypted += codebook[new_location]
            else:
                decrypted += codebook[new_location + max]
        else:
            decrypted += i
    return decrypted


if __name__ == "__main__":
    ##The following several lines generate the codebook
    ##Please don't change it
    random.seed("Caesar")
    
    codebook = []
    for e in string.ascii_letters:
        codebook.append(e)
        
    random.shuffle(codebook)
    print("Your codebook:")
    print(codebook)
    ## end of the codebook generation
    
    m = "Hello Kitty!"
    shift = 3
    encoded = caesarEncrypt(m, codebook, shift)
    decoded = caesarDecrypt(encoded, codebook, shift)
    print("Origin:", m)
    print("Encoded:", encoded)
    print("Decoded", decoded)