def string(n):
    if n == 1:
        return [['0'], ['1']]

    lst = string(n-1)

    for i in lst[:]:

        if i[-1] == '1':
            i.append('0')

        else:
            new_i = i[:]
            new_i.append('1')
            i.append('0')
            lst.append(new_i)


    return lst


def b_string(L):
    L = string(L)
    lst = []
    for i in L:
        lst.append(''.join(i))

    return lst

print(string(4))
print(b_string(4))