def travel(m, n):
    lst = route(m, n)
    #for i in lst[:]:
        #if len(i) != (m + n):
            #lst.remove(i)
    return lst




def route(m, n):
    import random
    if m == n == 0:
        return [[]]

    lst = []
    while not(m == n == 0):
        for i in range(2):
            if i == 1 and m != 0:
                m -= 1
            elif i == 1 and m == 0 and n != 0:
                i = 0
                n -= 1
            elif i == 0 and n != 0:
                n -= 1
            elif i == 0 and n == 0 and m != 0:
                i = 1
                m -= 1
            else:
                continue
            #print(lst)
            lst += [[i] + t for t in route(m, n)]


    return lst


def find_route(m, n):
    if m == n == 0:
        return [[]]
    lst = []
    plst = find_route()
    for i in range(2):




print(travel(2,2))