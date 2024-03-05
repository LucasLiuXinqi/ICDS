def is_lst(L):
    if type(L) == list:
        return True
    else:
        return False

def nest(L):
    lst = []
    for i in L:
        if is_lst(i):
            lst += nest(i)
        else:
            lst += [i]
    return lst

print(nest([[1, 2],[3,[4]],5]))