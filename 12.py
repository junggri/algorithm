input = [1, 2, 3, 4]
output = [24, 12, 8, 6]


# O(n)에 풀어라
#
def multi(nums):
    multi_num = 1
    multi_num_arr = []
    for i in range(len(nums)):
        multi_num_arr.append(multi_num)
        multi_num = multi_num * nums[i]

    multi_num = 1

    for i in range(len(multi_num_arr) - 1, - 1, -1):
        print(i)
        multi_num_arr[i] = multi_num_arr[i] * multi_num
        multi_num *= nums[i]
    # for j in range(len(multi_num_arr)):
    #     multi_num_arr[len(multi_num_arr) - 1 - j] = multi_num_arr[len(multi_num_arr) - 1 - j] * multi_num
    #     multi_num = multi_num * nums[len(nums) - 1 - j]
    print(multi_num_arr)


multi(input)

# for i in range(len(input)):
#     print(len(input) - i)
