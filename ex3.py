def fibonacci_main_recursion(n):
    """Основна рекурсивна функція для обчислення числа Фібоначчі."""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_main_recursion(n - 1) + fibonacci_main_recursion(n - 2)


def fibonacci_tail_recursion(n, a=0, b=1):
    """Хвостова рекурсивна функція для обчислення числа Фібоначчі."""
    if n == 0:
        return a
    elif n == 1:
        return b

    return fibonacci_tail_recursion(n - 1, b, a + b)


fibonacci_n = int(input('Enter a number: '))

print(fibonacci_tail_recursion(fibonacci_n))
print(fibonacci_main_recursion(fibonacci_n))
