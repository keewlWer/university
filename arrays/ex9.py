def replace_elements(arr):
    n = len(arr)
    max_right = -1

    for i in range(n - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)

    return arr

# Приклади використання
arr = [17, 18, 5, 4, 6, 1]
print(replace_elements(arr))  # [18, 6, 6, 6, 1, -1]

arr = [400]
print(replace_elements(arr))  # [-1]
