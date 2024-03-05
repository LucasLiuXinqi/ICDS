#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:48:42 2021

@author: bing
"""
def fraction2binary(f, space):
    ##complete the code
    b = ''
    i = 0
    while i < space:
        b += str(int(f * 2))
        f = f * 2 % 1
        i += 1
    return '0.'+b


def binary2fraction(b):
    ##complete the code
    bi = b[2:]
    sum = 0
    power = len(b[2:]) - 1
    for i in bi:
        sum += int(i) * (2 ** power)
        power -= 1
    num = sum / 2 ** len(b[2:])
    return num


if __name__ =='__main__':
    print('2.07 - 2 =', 2.07 - 2)
    f = 0.07
    l = 52
    print('The binary of 0.07 in your machine:')
    print(fraction2binary(f, l))
    print('Influence of the Truncation error')
    print(binary2fraction(fraction2binary(f, l)))
    
