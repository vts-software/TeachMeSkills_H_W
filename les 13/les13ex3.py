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
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        # Пример логики: если есть бекон, убираем пепперони
        if self.pepperoni:
            print("Есть бекон, убираем пепперони для баланса мяса.")
            self.pepperoni = False
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


# Директор
class PizzaDirector:
    TOPPING_METHODS = {
        "cheese": "add_cheese",
        "pepperoni": "add_pepperoni",
        "mushrooms": "add_mushrooms",
        "onions": "add_onions",
        "bacon": "add_bacon"
    }

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, toppings):
        for t in toppings:
            method_name = self.TOPPING_METHODS.get(t.lower())
            if method_name:
                getattr(self.builder, method_name)()
            else:
                raise ValueError(f"Неизвестная добавка: {t}")
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
