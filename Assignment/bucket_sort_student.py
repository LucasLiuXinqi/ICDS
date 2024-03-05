import random
random.seed(0)

def bucket_sort(mylist):
    # initialize the buckets
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

def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 100) for i in range(100)]
    """
    list_a = []
    for i in range(100):
        list_a.append(random.randint(0,100))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)    

main()
