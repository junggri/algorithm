input = [-1, 0, 1, 2, -1, -4]


def findZero(list):
    for i in range(len(list) - 1):
        # print(i)
        for j in range(i + 1, len(list)):
            find_num = -(list[i] + list[j])
            if find_num in list[j + 1:]:
                print(find_num, i, j)


findZero(input)
