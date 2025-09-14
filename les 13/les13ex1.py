def fibonacci(n):
    """
    Генератор чисел Фибоначчи.
    Он по очереди 'выдаёт' числа, а не хранит их все сразу.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    try:
        user_input = input("Введите номер числа Фибоначчи, до которого нужно выводить: ")
        n = int(user_input)

        if n <= 0:
            print("Нужно ввести положительное число больше нуля.")
            return

        print(f"Последовательность Фибоначчи до {n}-го числа:")
        for num in fibonacci(n):
            print(num, end=" ")

    except ValueError:
        print("Ошибка: нужно ввести целое число!")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
