def merge(lst_1, lst_2, mc):
    lst_3 = []
    r_cnt = 0
    while len(lst_1) != 0 and len(lst_2) != 0:
        if lst_1[0] > lst_2[0]:
            lst_3.append(lst_2.pop(0))
            r_cnt += 1
        else:
            lst_3.append(lst_1.pop(0))
            mc += r_cnt

    while len(lst_1) != 0:
        lst_3.append(lst_1.pop(0))
        mc += r_cnt

    while len(lst_2) != 0:
        lst_3.append(lst_2.pop(0))

    return lst_3, mc



def merge_sort(m):
    if len(m) == 1:
        mc = 0
        return m, mc
    else:
        mid = len(m) // 2
        left = m[:mid]
        right = m[mid:]
        left, lc = merge_sort(left)
        right, rc = merge_sort(right)

        final, mc = merge(left, right, mc)

    return final, lc+rc+mc

print(merge_sort([1,4,6,3,2]))