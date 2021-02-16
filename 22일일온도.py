class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []

        def findTemp(temp, list):
            count = 0
            if not list:
                return 0

            for t in list:
                if t > temp:
                    count = T.index(t) - T.index(temp)
                    return count
            return count

        for temp in range(0, len(T)):
            stack.append(findTemp(T[temp], T[temp + 1:]))
        return stack


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        arr = [0] * len(T)
        for i, temp in enumerate(T):
            print(i, temp)
            while stack and temp > T[stack[-1]]:
                idx = stack.pop()
                arr[idx] = i - idx

            stack.append(i)
        return arr


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []

        def findTemp(temp, idx, list):
            count = 0
            if not list:
                return 0
            for i,t in enumerate(list):
                if t > temp:
                    count =i+len(T[:idx+1])-idx
                    return count
            return count

        for idx in range(0, len(T)):
            stack.append(findTemp(T[idx], idx, T[idx + 1:]))
        return stack

//중복제거