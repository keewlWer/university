def climb_stairs_main_recursion(n):
    """Основна рекурсивна функція для обчислення кількості унікальних комбінацій підняття по сходах."""
    if n == 0:
        return 1
    elif n == 1:
        return 1

    return climb_stairs_main_recursion(n - 1) + climb_stairs_main_recursion(n - 2)


def climb_stairs_tail_recursion(n, prev1=1, prev2=1):
    """Хвостова рекурсивна функція для обчислення кількості унікальних комбінацій підняття по сходах."""
    if n == 0:
        return prev1
    elif n == 1:
        return prev2

    return climb_stairs_tail_recursion(n - 1, prev2, prev1 + prev2)


stairs_num = int(input('Enter number of stairs: '))


print('Всього унікальних варіантів:', climb_stairs_main_recursion(stairs_num))
print(climb_stairs_tail_recursion(stairs_num))