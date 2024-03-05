def powerset(L):
    import copy
    if len(L) == 0:
        return [[]]

    pset = powerset(L[1:])
    sub_set = copy.deepcopy(pset)
    for t in sub_set:
        t.append(L[0])
    pset.extend(sub_set)

    return pset

print(powerset([0,1,2]))