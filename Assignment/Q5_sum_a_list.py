#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:17:19 2022

@author: bing
"""

def sum_a_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        n = lst.pop(0)
        return n + sum_a_list(lst)


if __name__ == "__main__":
    
    print(sum_a_list([5, 4, 3, 2, 1]))