def check_if_exist(arr):
    seen = set()

    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)

    return False

# Приклади використання
arr = [10, 2, 5, 3]
print(check_if_exist(arr))  # True

arr = [3, 1, 7, 11]
print(check_if_exist(arr))  # False
