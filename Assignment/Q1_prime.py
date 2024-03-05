def is_prime(n):
    div = 0
    for j in range(1,n):
        if n % j == 0:
            div += 1
    if div == 1:
        return True
    else:
        return False

if __name__ == "__main__":

    def list_prime(n):
        p = []
        for i in range(1, n):
            if is_prime(i):
                p.append(i)
        return p

    print(list_prime(10000))