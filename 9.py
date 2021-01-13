list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = []


def rain(list):
    count = 0
    while sum(list) > 0:
        a = []
        for i in range(len(list)):
            if list[i] == 0:
                a.append(0)
            else:
                a.append(1)
                list[i] -= 1
        print(a)
        for i in range(len(a) - 1):
            zero_count = 0
            left = i
            right = i + 1
            if a[left] == 1 and a[right] == 0:
                zero_count += 1
                right += 1
                while right < len(a):
                    if a[right] == 1:
                        count += zero_count
                        break
                    else:
                        zero_count += 1
                        right += 1

    return count


a = rain(list)

# list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = []


def trapping(list):
    left, right = 0, len(list) - 1
    left_max, right_max = list[left], list[right]
    count = 0
    while left < right:
        left_max = max(left_max, list[left])
        right_max = max(right_max, list[right])
        if left_max <= right_max:
            count += left_max - list[left]
            left += 1
        else:
            count += right_max - list[right]
            right -= 1
    print(count)
    return count
