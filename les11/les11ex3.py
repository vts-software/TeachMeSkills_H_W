# Программа с классом Car. При инициализации объекта
# ему должны задаваться атрибуты color, type и year.
# Реализовать пять методов. Запуск автомобиля – выводит
# строку «Автомобиль заведён». Отключение автомобиля –
# выводит строку «Автомобиль заглушен». Методы для
# присвоения автомобилю года выпуска, типа и цвета.
class Car:

    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведён")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска установлен: {self.year}")

    def set_type(self, car_type):
        self.car_type = car_type
        print(f"Тип автомобиля установлен: {self.car_type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")

# Метод __str__
    def __str__(self):
        return f"Цвет: {self.color}, Тип: {self.car_type}, Год: {self.year}"

# # Метод __repr__
#     def __repr__(self):
#         return f"Car(color='{self.color}', car_type='{self.car_type}', year={self.year})"

color = input("Введите цвет автомобиля: ")
car_type = input("Введите тип автомобиля (седан, хэтчбек, внедорожник и т.д.): ")

while True:
    try:
        year = int(input("Введите год выпуска автомобиля (число): "))
        break

    except ValueError:
        print("Ошибка: введите год числом!")

my_car = Car(color, car_type, year)

print("\nМашина создана!")
print(my_car)

# --- Интерактивная панель ---
while True:
    print("\nЧто хотите сделать?")
    print("1 — Завести машину")
    print("2 — Заглушить машину")
    print("3 — Изменить цвет")
    print("4 — Изменить тип")
    print("5 — Изменить год выпуска")
    print("6 — Показать свойства машины")
    print("0 — Выйти")

    choice = input("Ваш выбор: ")


    if choice == "1":
        my_car.start_engine()

    elif choice == "2":
        my_car.stop_engine()

    elif choice == "3":
        new_color = input("Введите новый цвет: ")
        my_car.set_color(new_color)

    elif choice == "4":
        new_type = input("Введите новый тип: ")
        my_car.set_type(new_type)

    elif choice == "5":

        try:
            new_year = int(input("Введите новый год: "))
            my_car.set_year(new_year)

        except ValueError:
            print("Ошибка: год должен быть числом!")

    elif choice == "6":
        print("Свойства машины:", my_car.color, my_car.car_type, my_car.year)

    elif choice == "0":
        print("Выход из программы...")
        break

    else:
        print("Неверный выбор, попробуйте снова.")