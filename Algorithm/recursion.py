def permute(nums):
    # put your code here

    pass
    lst = []
    if len(nums) == 1:

        return [nums]
    for i in range(len(nums)):
        num = nums.copy()
        e = num.pop(i)
        lst += [[e] + t for t in permute(num)]

    return lst
# tests

if __name__ == "__main__":
    nums = [1, 2, 3]
    p1 = permute(nums)
    print("Permutation:", p1)

    nums = ['a', 'b', 'c', 'd']
    p2 = permute(nums)
    print("Permutation:", p2)
