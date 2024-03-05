def remove_non_int(L):
    int_index = 0
    for i in range(len(L)):
        if type(L[i]) == int:
            L[int_index] = L[i]
            int_index += 1
        # print(L)
    return L[:int_index]

L = [1, 2.2, 3, 4.4, 5]
print(remove_non_int(L))
