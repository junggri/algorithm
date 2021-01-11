s = "ababd"


#


#
# word_dict = collections.defaultdict(list)
# start = time.time()
# for num in range(1, len(list(s)) + 1):
#     if num == 5:
#         break
#     for num2 in range(0, num):
#         word = s[num2:len(s) - num + num2 + 1]
#         if word == word[::-1]:
#             word_dict[len(word)].append(word)
#
# for word in word_dict[list(word_dict)[0]]:
#     print("\"%s\"" % word)
#
# sec = time.time()

# def longestPenlindrom(s):
#     def expand(left, right):
#         while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
#             left -= 1
#             right += 1
#         return s[left + 1:right - 1]
#
#     if len(s) < 2 or s == s[::-1]:
#         return s
#     result = ""
#     for i in range(len(s) - 1):
#         result = max(result, expand(i, i + 1), expand(i, i + 2), key=lambda x: len(x))
#
#     return result
#
#
# a = longestPenlindrom('babad')
# print(a)

# print(range(0, 5))


# c = collections.Counter
#
#
def pelindrome(s, space):
    arr = []
    for i in range(0, (len(s) - space)):
        left = i
        right = i + space
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                arr.append(s[left:right + 1])
                left -= 1
                right += 1
            else:
                left += 1
                right += 1
    return arr


# 내풀이 의 문제점은 기준점으로 확장해나가고 끝내야할것을 i=0부터 시작해서 3까지 다 확인하고 잇는것이 문ㅈ욨다
# i=0일떄는 기준점만 확인하고 다음 i로 넘어가야한다

a = (pelindrome(s, 1))
b = (pelindrome(s, 2))
#
print(a, b)
# print(max(a + b, key=len))
