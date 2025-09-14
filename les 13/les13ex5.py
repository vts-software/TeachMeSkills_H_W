# Паттерн «Стратегия»
# ● Создайте класс Calculator, который использует разные
# стратегии для выполнения математических операций.
# ● Создайте несколько классов, каждый реализует
# определенную стратегию математической операции,
# например, Addition, Subtraction, Multiplication, Division.
# Каждый класс должен содержать метод execute, который
# принимает два числа и выполняет соответствующую
# операцию.
# ● Calculator должен иметь метод set_strategy, который
# устанавливает текущую стратегию, и метод calculate,
# который выполняет операцию с помощью текущей стратегии.
class OperationStrategy:
    """
    Общий шаблон (интерфейс) для всех стратегий.
    У каждой стратегии будет метод execute, который выполняет математическую операцию.
    """
    def execute(self, a, b):
        raise NotImplementedError("Нужно переопределить метод execute в дочернем классе")


class Addition(OperationStrategy):
    """Класс для сложения"""
    def execute(self, a, b):
        return a + b


class Subtraction(OperationStrategy):
    """Класс для вычитания"""
    def execute(self, a, b):
        return a - b


class Multiplication(OperationStrategy):
    """Класс для умножения"""
    def execute(self, a, b):
        return a * b


class Division(OperationStrategy):
    """Класс для деления"""
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return a / b


class Calculator:
    """
    Калькулятор, который может использовать разные стратегии.
    """
    def __init__(self):
        self.strategy = None  # изначально стратегия не выбрана

    def set_strategy(self, strategy):
        """Устанавливаем стратегию (например, сложение или деление)"""
        self.strategy = strategy

    def calculate(self, a, b):
        """Выполняем выбранную стратегию"""
        if not self.strategy:
            raise ValueError("Стратегия не установлена!")
        return self.strategy.execute(a, b)


# Пример использования
if __name__ == "__main__":
    calc = Calculator()

    try:
        calc.set_strategy(Addition())
        print("5 + 3 =", calc.calculate(5, 3))

        calc.set_strategy(Subtraction())
        print("5 - 3 =", calc.calculate(5, 3))

        calc.set_strategy(Multiplication())
        print("5 * 3 =", calc.calculate(5, 3))

        calc.set_strategy(Division())
        print("5 / 0 =", calc.calculate(5, 0))  # тут вызовет ошибку

    except ZeroDivisionError as e:
        print("Ошибка:", e)
    except ValueError as e:
        print("Ошибка:", e)
    except Exception as e:
        print("Неожиданная ошибка:", e)
