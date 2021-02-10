class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for i in s:
            if not i in stack:
                stack.append(i)
        return "".join(sorted(stack))
