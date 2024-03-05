def linear_search(L, x):
    if len(L) == 1:
        if L[0] == x:
            return True
        else:
            return False
    else:
        if L[0] == x:
            return True
        else:
            return linear_search(L[1:], x)

print(linear_search([0, 1, 5, 7, 9, 11, 12, 12, 12, 17, 17, 18, 26, 27, 32, 33, 33, 36, 38, 39, 40, 42, 45, 45, 49, 51, 51, 53, 55, 56, 60, 61, 61, 62, 63, 64, 65, 66, 68, 70, 70, 71, 74, 77, 78, 78, 79, 80, 81, 85, 87, 90, 90, 92, 93, 96, 97, 100, 109], 108))