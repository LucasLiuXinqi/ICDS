def combine(lst_1, lst_2):
    if len(lst_2) < len(lst_1):
        lst_1, lst_2 = lst_2, lst_1
    lst_3 = []


    while len(lst_1) != 0 and len(lst_2) != 0:
        lst_3.append(lst_1.pop(0))
        lst_3.append(lst_2.pop(0))

    while len(lst_1) != 0:
        lst_3.append(lst_1.pop(0))

    while len(lst_2) != 0:
        lst_3.append(lst_2.pop(0))
    #print(lst_3)
    return LCS(lst_3)


def split(str_1, str_2):
    lst_1 = []
    lst_2 = []
    lst_1 += str_1
    lst_2 += str_2

    return combine(lst_1, lst_2)


def LCS(L):
    idx = 0
    idx = 0
    for i in range(len(L) - 1):
        if L[i] != L[i+1]:
            L[idx] = L[i]
            idx += 1
            #print(idx)
        #print(L)
    if L[-1] != L[idx-1]:
        L[idx] = L[-1]
    return ''.join(L[:idx + 1])





print(split('ABCDA', 'CBCDAB'))