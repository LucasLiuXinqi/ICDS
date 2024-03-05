#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:57 2021

@author: bing
"""


def permute(nums):
    # put your code here

    pass
    lst = []
    if len(nums) == 1:

        return [nums]
    for i in range(len(nums)):
        num = nums.copy()
        e = num.pop(i)
        print('after pop', num, nums, i)
        pm = permute(num)
        print('after pm', pm)
        lst += [[e] + t for t in pm]

    return lst
# tests

if __name__ == "__main__":
    nums = [1, 2, 3]
    p1 = permute(nums)
    print("Permutation:", p1)

    nums = ['a', 'b', 'c', 'd']
    p2 = permute(nums)
    print("Permutation:", p2)
