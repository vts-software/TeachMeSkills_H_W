# ПчёлоСлон
# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону. Класс реализует
# следующие методы:
# ● fly() – возвращает True, если часть пчелы не меньше части
# слона, иначе – False
# ● trumpet() – если часть слона не меньше части пчелы,
# возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
# ● eat(meal, value) – может принимать в meal только ”nectar”
# или “grass”. Если съедает нектар, то value вычитается из
# части слона, пчеле добавляется. Иначе – наоборот. Не
class PcheloSlon:
    def __init__(self, bee_part, elephant_part):
        # Проверяем, что оба параметра — целые числа
            if not isinstance(bee_part, int) or not isinstance(elephant_part, int):
                raise TypeError("Оба параметра должны быть целыми числами.")
            if not (0 <= bee_part <= 100) or not (0 <= elephant_part <= 100):
                raise ValueError("Начальные значения должны быть от 0 до 100.")
            self.bee = bee_part
            self.elephant = elephant_part

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal, value):
        if meal not in ("nectar", "grass"):
            raise ValueError("meal должен быть 'nectar' или 'grass'")
        if not isinstance(value, int):
            raise TypeError("value должен быть целым числом")
        if value < 0:
            raise ValueError("value должен быть неотрицательным")

        if meal == "nectar":
            if value > self.elephant:
                raise ValueError("У слона недостаточно части, чтобы отдать столько nectar")
            self.elephant -= value
            self.bee += value
        else:  # grass
            if value > self.bee:
                raise ValueError("У пчелы недостаточно части, чтобы отдать столько grass")
            self.bee -= value
            self.elephant += value

    def __str__(self):
        return f"Пчела: {self.bee}, Слон: {self.elephant}"


# ---- Пользовательский ввод ----

print("=== Создание ПчёлоСлона ===")
bee_start = int(input("Введите целое число — часть пчелы: "))
elephant_start = int(input("Введите целое число — часть слона: "))

ps = PcheloSlon(bee_start, elephant_start)
print("Создан:", ps)

while True:
    print("\nВыберите действие:")
    print("1 — Проверить fly()")
    print("2 — Проверить trumpet()")
    print("3 — Покормить (eat)")
    print("4 — Показать текущее состояние")
    print("0 — Выйти")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        print("Результат fly():", ps.fly())

    elif choice == "2":
        print("Результат trumpet():", ps.trumpet())

    elif choice == "3":
        meal = input("Введите тип еды (nectar/grass): ").strip()
        value = int(input("Введите количество: "))
        try:
            ps.eat(meal, value)
            print("После еды:", ps)
        except Exception as e:
            print("Ошибка:", e)

    elif choice == "4":
        print(ps)

    elif choice == "0":
        print("Выход из программы...")
        break

    else:
        print("Неверный выбор, попробуйте снова.")
