
"""
Created on Feb 15, 2023
@Author: Hammond Liu
"""

# fib(5)
# -> fib(4) + fib(3)
# -> (fib(3) + fib(2)) + (fib(2) + fib(1))
# -> ...
# -> sum of many fib(1) & fib(0)

def fib(n):
    # base case
    if n <= 1:
        return n
    # recursive branch
    else:
        return fib(n-1) + fib(n-2)

for i in range(5):
    print(i, fib(i))

# # sample 1: [1] -> 1 + func([])
# # sample 2: [1, 2] -> 1 + func([2])
# def sum_a_list(l):
#     # base case
#     if len(l) == 0:
#         print('base case')
#         return 0
#     # recursive branch
#     print('current l:', l)
#     return sum_a_list(l[1:]) + l[0]

# print(sum_a_list([1, 2, 3]))