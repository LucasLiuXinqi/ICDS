def merge(lst_1, lst_2):
    lst_3 = []
    while len(lst_1) != 0 and len(lst_2) != 0:
        if lst_1[0] > lst_2[0]:
            lst_3.append(lst_2.pop(0))
        else:
            lst_3.append(lst_1.pop(0))


    while len(lst_1) != 0:
        lst_3.append(lst_1.pop(0))

    while len(lst_2) != 0:
        lst_3.append(lst_2.pop(0))

    return lst_3



def merge_sort(m):
    if len(m) == 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

print(merge_sort([49, 97, 53, 5, 33, 65, 62, 51, 100, 38, 61, 45, 74, 27, 64, 17, 36, 17, 96, 12, 79, 32, 68, 90, 77, 18, 39, 12, 93, 9, 87, 42, 60, 71, 12, 45, 55, 40, 78, 81, 26, 70, 61, 56, 66, 33, 7, 70, 1, 11, 92, 51, 90, 100, 85, 80, 0, 78, 63]))