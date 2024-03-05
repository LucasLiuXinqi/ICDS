def delete_nonint(L):
    idx = 0
    for i in range(len(L)):
        if type(L[i]) == int:
            L[idx] = L[i]
            idx += 1

    for j in range(idx, len(L)):
        L.pop(-1)


L = [1,4,2.43,4.23,7,234.4,456]
delete_nonint(L)
print(L)