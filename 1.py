def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-z', '', s)
    s[::-1] = 뒺ㅂ어러
