#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:19 2020

@author: xg7
"""

def convert_to_Roman_numeral(n):
    ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    m = (n // 1000) * 'M'
    h = hundreds[(n % 1000) // 100]
    t = tens[(n % 100) // 10]
    o = ones[(n % 10)]
    rom = m + h + t + o
    return rom
##test
if __name__ == "__main__":
    n = 1800
    print(convert_to_Roman_numeral(n))


