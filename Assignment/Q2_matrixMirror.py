#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:45:08 2020

@author: xg7
"""

def fun1(m):
    for i in m:
        i = i.reverse()



##Tests
if __name__ == "__main__":
    n = 3
    m = [ [(i)*n + j + 1 for j in range(n)] for i in range(n) ]
    print("input m:", m)
    fun1(m)
    print("after running fun1:", m)

    n = 4
    m = [ [(i)*n + j + 1 for j in range(n)] for i in range(n) ]
    print("input m:", m)
    fun1(m)
    print("after running fun1:", m)
