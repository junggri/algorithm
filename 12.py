input = [1, 2, 3, 4]
output = [24, 12, 8, 6]


# O(n)에 풀어라
#
def multi(input):
    arr = []
    multi_num = 1
    for i in range(len(input)):
        arr.append(multi_num)
        multi_num *= input[i]
    print(arr)


multi(input)
