# Мы будем использовать функцию-генератор, которая создаёт бесконечную последовательность чисел.
# Генератор отличается от обычной функции тем, что он возвращает значения по одному (через yield),
# а не всё сразу. Это экономит память и позволяет "растягивать" вычисления во времени.

def cyclic_generator():
    """
    Генераторная функция для бесконечной последовательности 1-2-3-1-2-3...
    """
    numbers = [1, 2, 3]
    while True:
        for num in numbers:
            yield num


def main():
    try:
        count = int(input("Введите, сколько чисел вывести: "))
        if count <= 0:
            print("Нужно ввести положительное число!")
            return

        gen = cyclic_generator()

        result = []
        for _ in range(count):
            result.append(next(gen))

        print("Результат:", " ".join(map(str, result)))

    except ValueError:
        print("Ошибка: нужно вводить только целое число!")


if __name__ == "__main__":
    main()
