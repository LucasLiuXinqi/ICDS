def pick_k_elements(elements, k):
    lst = []
    if k == 0:
        return [[]]

    for i in range(len(elements)):
        elements_cpy = elements.copy()
        e = elements_cpy.pop(i)
        lst += [[e] + t for t in pick_k_elements(elements_cpy, k-1)]
    return lst


def permute(nums):
    lst = []
    if len(nums) == 1:

        return [nums]
    for i in range(len(nums)):
        num = nums.copy()
        e = num.pop(i)
        lst += [[e] + t for t in permute(num)]

    return lst





if __name__ == "__main__":

    a = [1, 2, 3]
    k = 2

    b = pick_k_elements(a, k)
    print(b)

    #
    # nums = [1, 2, 3]
    # p1 = pick_k_elements(nums)
    # print("Permutation:", p1)

    # nums = ['a', 'b', 'c', 'd']
    # p2 = permute(nums)
    # print("Permutation:", p2)
