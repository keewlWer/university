def valid_mountain_array(arr):
    n = len(arr)

    if n < 3:
        return False

    i = 0

    # Зростаюча частина
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Перевірка на пік
    if i == 0 or i == n - 1:
        return False

    # Спадна частина
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# Приклади використання
arr = [2, 1]
print(valid_mountain_array(arr))  # False

arr = [3, 5, 5]
print(valid_mountain_array(arr))  # False

arr = [0, 3, 2, 1]
print(valid_mountain_array(arr))  # True
