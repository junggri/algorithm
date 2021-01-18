input = [-1, 0, 1, 2, -1, -4]


def findZero(list):
    arr = []
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            find_num = -(list[i] + list[j])
            if find_num in list[j + 1:]:
                anw = sorted([list[i], list[j], find_num])
                if anw not in arr:
                    arr.append(anw)
    print(arr)


findZero(input)


def threeSum(self, nums):
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i + 1]:
            continue
    left, right = i, len(nums) - 1
    sum = nums[left] + nums[right] + nums[i]
    print(sum)
