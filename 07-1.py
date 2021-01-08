import time

start = time.time()
nums = [2, 7, 11, 15]
target = 9

for i in nums:
    if i > 9:
        del nums[nums.index(i)]

print(nums)
end_time = time.time()
print("WorkingTime: {} sec".format(end_time - start))
