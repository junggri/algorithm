# def reorderLogFiles(logs):
#     digits = []
#     letters = []
#     for i in logs:
#         if i.split()[1].isdigit():
#             digits.append(i)
#         else:
#             letters.append(i)
#
#     digits.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#     letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#     print((digits, letters))
#
#
# reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
s = ['2 a', '1 b', '4 c', '1 a']
b = sorted(s, key=lambda x: x.split()[1])
c = sorted(b, key=lambda x: x.split()[0])
print(c)
