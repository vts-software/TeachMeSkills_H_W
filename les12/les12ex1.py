# Класс «Товар» содержит следующие закрытые поля:
# ● название товара
# ● название магазина, в котором подаётся товар
# ● стоимость товара в рублях
# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# ● вывод информации о товаре со склада по индексу
# ● вывод информации о товаре со склада по имени товара
# ● сортировка товаров по названию, по магазину и по цене
# ● перегруженная операция сложения товаров по цене
class Product:

    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def get_name(self):
        return self.__name

    def get_shop(self):
        return self.__shop

    def get_price(self):
        return self.__price

    def print_info(self):
        print(f"Название: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price} руб.")

    def __add__(self, other):
        return self.__price + other.__price


class Warehouse:
    def __init__(self):
        self.__items = []

    def add(self, product):
        self.__items.append(product)

    def print_by_index(self, index):

        if 0 <= index < len(self.__items):
            self.__items[index].print_info()

        else:
            print("Неправильный индекс")

    def print_by_name(self, name):
        found = False

        for item in self.__items:

            if item.get_name() == name:
                item.print_info()
                found = True

        if not found:
            print("Товар с таким именем не найден")

    def sort_by_name(self):
        self.__items.sort(key=lambda p: p.get_name())

    def sort_by_shop(self):
        self.__items.sort(key=lambda p: p.get_shop())

    def sort_by_price(self):
        self.__items.sort(key=lambda p: p.get_price())

    def print_all(self):

        if not self.__items:
            print("Склад пуст")
            return

        for i, item in enumerate(self.__items):
            print(f"{i}: ", end="")
            item.print_info()

    def size(self):
        return len(self.__items)

    def get_item(self, index):

        if 0 <= index < len(self.__items):
            return self.__items[index]

        return None


if __name__ == "__main__":
    w = Warehouse()

    while True:
        print("\nМеню:")
        print("1. Добавить товар")
        print("2. Показать все товары")
        print("3. Показать товар по индексу")
        print("4. Показать товар по имени")
        print("5. Сортировать по названию")
        print("6. Сортировать по магазину")
        print("7. Сортировать по цене")
        print("8. Сложить цены двух товаров")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название товара: ")
            shop = input("Введите название магазина: ")


            while True:
                price_str = input("Введите цену товара (число) руб: ")

                try:

                    if "." in price_str:
                        price = float(price_str)

                    else:
                        price = int(price_str)

                    break

                except ValueError:
                    print("Ошибка! Введите число (например: 50 или 49.9)")

            w.add(Product(name, shop, price))
            print("Товар добавлен!")

        elif choice == "2":
            w.print_all()

        elif choice == "3":
            idx = int(input("Введите индекс товара: "))
            w.print_by_index(idx)

        elif choice == "4":
            name = input("Введите название товара: ")
            w.print_by_name(name)

        elif choice == "5":
            w.sort_by_name()
            print("Отсортировано по названию!")

        elif choice == "6":
            w.sort_by_shop()
            print("Отсортировано по магазину!")

        elif choice == "7":
            w.sort_by_price()
            print("Отсортировано по цене!")

        elif choice == "8":

            if w.size() < 2:
                print("Недостаточно товаров для сложения!")

            else:
                idx1 = int(input("Введите индекс первого товара: "))
                idx2 = int(input("Введите индекс второго товара: "))
                item1 = w.get_item(idx1)
                item2 = w.get_item(idx2)

                if item1 and item2:
                    print(f"Сумма цен: {item1 + item2} руб.")

                else:
                    print("Неверный индекс!")

        elif choice == "0":
            print("Выход из программы.")

            break

        else:
            print("Неверный выбор, попробуйте снова.")
