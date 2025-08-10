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
        if b == 0:  # Проверяем, чтобы не делить на 0
            print("Ошибка: Деление на ноль невозможно!")
        else:
            result = a / b  # Считаем частное
            print(f"Частное: {result}")  # Выводим результат


math_obj = Math()

# Пользовательский ввод
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вызываем методы и показываем результаты
math_obj.addition(num1, num2)
math_obj.subtraction(num1, num2)
math_obj.multiplication(num1, num2)
math_obj.division(num1, num2)
