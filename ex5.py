def pow_main_recursion(x, n):
    """Основна рекурсивна функція для піднесення x до ступеня n."""
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        half_pow = pow_main_recursion(x, n // 2)
        return half_pow * half_pow
    else:
        return x * pow_main_recursion(x, n - 1)


def pow_tail_recursion(x, n, acc=1):
    """Хвостова рекурсивна функція для піднесення x до ступеня n."""
    if n == 0:
        return acc

    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        return pow_tail_recursion(x * x, n // 2, acc)
    else:
        return pow_tail_recursion(x, n - 1, acc * x)


x = int(input("Введіть число, яке ви хочете піднести в ступінь: "))
n = int(input("Введіть ступінь в який ви хочете піднести число: "))
print(pow_tail_recursion(x, n))
print(pow_main_recursion(x, n))
