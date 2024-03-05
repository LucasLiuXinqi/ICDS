def fib(n):
    lst = []
    if n == 1:
        return 1
    if n == 2:
        return 1

    m = fib(n - 2) + fib(n - 1)

    return m


print(fib(5))


