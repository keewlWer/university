import random


def generate_random_binary_array(size):
    binary_array = [random.randint(0, 1) for _ in range(size)]
    print(f"Random binary array: {binary_array}")
    return binary_array


def get_number_of_ones_in_the_row(binary_array: list) -> int:
    max_count = 0
    current_count = 0

    for i in binary_array:
        if i == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


def main() -> None:
    while True:
        try:
            length = int(input("Введите размер массива (1 - 100000): ").strip())
            binary_array = generate_random_binary_array(length)
            print(get_number_of_ones_in_the_row(binary_array))

        except ValueError:
            print("Ошибка, неверный тип данных. Попробуйте ввести еще раз.")


if __name__ == "__main__":
    main()
