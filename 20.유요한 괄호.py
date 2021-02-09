input = "()[]{}((()){}}{"

print(sorted(input))


def isValid(input):
    stack = []
    table = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    # 테이블을 수동적으로 만드는 방법이라 좋은 방법은 아나라고본다
    for i in input:
        if i in table:
            stack.append(table[i])
        elif not stack and stack.pop() != table[i]:
            return False
    return True


a = isValid(input)
print(a)
