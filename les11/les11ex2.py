#  Напишите программу с классом Math. При
# инициализации атрибутов нет. Реализовать методы addition,
# subtraction, multiplication и division. При передаче в методы
# двух числовых параметров нужно производить с
# параметрами соответствующие действия и печатать ответ.
class Math:

    def __init__(self):
        pass  # Ничего не сохраняем

    def addition(self, a, b):
        result = a + b  # Считаем сумму
        print(f"Сумма: {result}")  # Выводим результат

    def subtraction(self, a, b):
        result = a - b  # Считаем разность
        print(f"Разность: {result}")  # Выводим результат

    def multiplication(self, a, b):
        result = a * b  # Считаем произведение
        print(f"Произведение: {result}")  # Выводим результат

    def division(self, a, b):
        try:
            result = a / b
            print(f"Частное: {result}")

        except ZeroDivisionError:
            print("Ошибка: Деление на ноль невозможно!")
        else:
            result = a / b  # Считаем частное
            print(f"Частное: {result}")  # Выводим результат


math_obj = Math()

# Пользовательский ввод
while True:
    try:
        num1 = float(input("Введите первое число: "))
        break

    except ValueError:
        print("Ошибка: нужно ввести число!")

while True:
    try:
        num2 = float(input("Введите второе число: "))
        break

    except ValueError:
        print("Ошибка: нужно ввести число!")

# Вызываем методы и показываем результаты
math_obj.addition(num1, num2)
math_obj.subtraction(num1, num2)
math_obj.multiplication(num1, num2)
math_obj.division(num1, num2)
