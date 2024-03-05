def prime(n, m):
    if m == 1:
        return 1
    if n % m == 0:
        return 1 + prime(n, m-1)
    else:
        return 0 + prime(n, m-1)


def find(n):

    if n == 1:
        return []
    if prime(n, n) == 2:
        return find(n-1) + [n]
    else:
         return find(n-1)




print(find(30))