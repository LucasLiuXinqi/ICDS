def split(L):
    pivot, lst = L[0], L[1:]
    left_lst = [i for i in lst if i <= pivot]
    right_lst = [i for i in lst if i > pivot]

    return left_lst, pivot, right_lst

def quick_sort(L):
    if len(L) <= 1:
        return L

    left_lst, pivot, right_lst = split(L)

    left_lst = quick_sort(left_lst)
    right_lst = quick_sort(right_lst)

    return left_lst + [pivot] + right_lst

#print(quick_sort([9, 7, 6, 4, 2, 7, 8, 13, 1]))


def sub_lst(L):
    if len(L) == 0:
        return [[]]

    lst = []

    for i in range(len(L)):
        L_copy = L[:]
        m = L_copy.pop(i)
        lst += [[m] + i for i in sub_lst(L_copy)]

    return lst

#print(sub_lst([1,2,3]))

def powerset(L):
    if len(L) < 1:
        return [[]]

    lst = []
    pre_lst = powerset(L[1:])
    print(pre_lst)
    lst += [[L[0]] + i for i in pre_lst] + pre_lst

    return lst

print(powerset([1,2,3]))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

#print(fib(6))

