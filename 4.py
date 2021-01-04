import collections
import re

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
banned = ['hit']

word2 = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]
print(word2)

most, count = ("", 0)

for a in word2:
    count2 = word2.count(a)
    if count2 > count:
        most = a
        count = count2
print(most, count)

# 내 풀이
word = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]

count = collections.defaultdict(lambda: 0)
for word in word:
    count[word] += 1
print(count)
