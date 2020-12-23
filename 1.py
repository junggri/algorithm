"""
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-z', '', s)
    s[::-1] = 뒺ㅂ어러
"""

# f = open("./새파일.txt", "w")
# for i in range(1, 11):
#     data = f'{i + 1}\n'
#     f.write(data)
# f.close()

f = open("./새파일.txt", 'r')
data = f.read()
print(data)
f.close()
