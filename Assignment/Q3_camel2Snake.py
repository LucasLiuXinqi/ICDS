#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:43:58 2020

@author: xg7
"""

def camel2snake():
    camel = str(input('Please input a camel: '))
    snake = ''
    for i in camel:
        if i.isupper():
            snake += '_'
            snake += i.lower()
        else:
            snake += i
    return snake




print(camel2snake())