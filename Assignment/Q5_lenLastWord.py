#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:48:59 2020

@author: xg7
"""

def lenLastWord(s):
    import string
    pun = string.punctuation
    for i in s:
        if i in pun:
            s = s.replace(i, ' ')
    start = 0
    word = ''
    for j in range(len(s)):
        if s[j] == ' ':
            if s[start:j].isalpha():
                word = s[start:j]
            start = j + 1
    return len(word)





##test
if __name__ == "__main__":
    
    s = "hello world."
    print(lenLastWord(s))
    
    s = "Good morning  !"
    print(lenLastWord(s))
   
