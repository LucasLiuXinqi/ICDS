import random
random.seed(0)

def get_pancake(a, b, n):
    return [random.randint(a, b) for i in range(n)]

def flip(L):
    max = L[0]
    idx = 0
    for i in range(1, len(L)):
        if L[i] >= max:
            max = L[i]
            idx = i

    lst_flip = L[0:idx + 1]
    lst = lst_flip[::-1] + L[idx+1:]

    return lst[::-1]



def pancakesort(L):

    if len(L) == 1:
        return [L[0]]
    L = flip(L)

    return pancakesort(L[:-1]) + [L[-1]]

L = get_pancake(1, 9, 5)
print('original', L)
print(pancakesort(L))