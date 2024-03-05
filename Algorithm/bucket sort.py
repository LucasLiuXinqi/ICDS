def bucket_sort(mylist):
    mydict = {}
    dict_num = max(mylist) // 10 + 1
    for i in range(10, (dict_num + 1)*10, 10):
        mydict[i] = mydict.get(i, [])
    for i in mylist:
        loc = (i // 10 + 1) * 10
        mydict[loc].append(i)
    result = []
    for element in mydict.values():
        element.sort()
        result += element

    return result