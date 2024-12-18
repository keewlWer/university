def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

# Приклади використання:

# Приклад 1
print(isValid("()"))  # Output: True

# Приклад 2
print(isValid("()[]{}"))  # Output: True

# Приклад 3
print(isValid("(]"))  # Output: False
