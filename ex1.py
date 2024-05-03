def reverse_string_main_recursion(s, index=0):
    """Рекурсивна функція для друку рядка в зворотному порядку за допомогою основної рекурсії."""
    if index == len(s):
        return
    reverse_string_main_recursion(s, index + 1)
    print(s[index], end='')


def reverse_string_tail_recursion(s, index=None, result=''):
    """Рекурсивна функція для друку рядка в зворотному порядку за допомогою хвостової рекурсії."""
    if index is None:
        index = len(s) - 1
    if index < 0:
        print(result, end='')
        return
    result += s[index]

    reverse_string_tail_recursion(s, index - 1, result)


string_to_reverse = input('Enter string to reverse: ')
reverse_string_main_recursion(string_to_reverse)
print('')
reverse_string_tail_recursion(string_to_reverse)
