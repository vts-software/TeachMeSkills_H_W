# === Паттерн "Строитель" для пиццы ===
class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = [name for name, flag in [
            ("сыр", self.cheese),
            ("пепперони", self.pepperoni),
            ("грибы", self.mushrooms),
            ("лук", self.onions),
            ("бекон", self.bacon)
        ] if flag]
        return f"Пицца {self.size} — {', '.join(toppings) if toppings else 'без добавок'}"


# Строитель
class PizzaBuilder:
    VALID_SIZES = ("small", "medium", "large")

    def __init__(self, size):
        size = size.lower()
        if size not in self.VALID_SIZES:
            raise ValueError(f"Неверный размер. Допустимые: {self.VALID_SIZES}")
        self.size = size
        self.cheese = self.pepperoni = self.mushrooms = self.onions = self.bacon = False

    def add(self, topping):
        if topping == "cheese": self.cheese = True
        elif topping == "pepperoni": self.pepperoni = True
        elif topping == "mushrooms": self.mushrooms = True
        elif topping == "onions": self.onions = True
        elif topping == "bacon": self.bacon = True
        else:
            raise ValueError(f"Неизвестная добавка: {topping}")
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


# Директор
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, toppings):
        for t in toppings:
            self.builder.add(t.lower())
        return self.builder.build()


if __name__ == "__main__":
    try:
        size = input("Введите размер пиццы (small, medium, large): ")
        toppings = input("Введите добавки через запятую (cheese, pepperoni, mushrooms, onions, bacon): ")
        toppings_list = [t.strip().lower() for t in toppings.split(",") if t.strip()]

        builder = PizzaBuilder(size)
        director = PizzaDirector(builder)
        pizza = director.make_pizza(toppings_list)

        print("\nВаша пицца готова!")
        print(pizza)

    except Exception as e:
        print("Ошибка:", e)
