num2 = [2, 7, 11, 15]
target = 9


# for i in range(len(num2)):
#     for j in range(i + 1, len(num2)):
#         if num2[i] + num2[j] == 9:
#             print(num2[i], num2[j])
#

def twoSum(nums, target):
    for i, n in enumerate(nums):
        complemnet = target - n

        if complemnet in nums[i + 1:]:
            print(nums.index(n), nums[i + 1:].index(complemnet) + (i + 1))


twoSum(num2, target)
