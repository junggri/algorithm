import sys

nums = [7, 1, 5, 3, 10, -1, 8]


def SellMax(nums):
    smallest = min(nums)
    biggest = max(nums[nums.index(smallest):])
    print(min(nums))
    print(biggest - smallest)
    return biggest - smallest


SellMax(nums)


def profit(num):
    biggest = -sys.maxsize
    smallest = sys.maxsize

    for i in num:
        # 0,1, 2, 3, 4, 5,

        smallest = min(smallest, i)
        biggest = max(biggest, i - smallest)

    print(biggest)


profit(nums)
