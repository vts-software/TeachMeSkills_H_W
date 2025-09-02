# Создайте класс Soda (газировка). Для инициализации
# есть параметр, который определяет вкус газировки.
class Soda:
    def __init__(self, taste=None):
        self.taste = taste  # Сохраняем вкус в объекте

    def __str__(self):
        if self.taste:  # Если вкус задан (не пустой)
            return f"У вас газировка с {self.taste} вкусом"

        else:  # Если вкус не задан
            return "У вас обычная газировка"


user_input = input("Введите вкус газировки (оставьте пустым, если обычная): ").strip()


if user_input == "":
    soda = Soda()

else:
    soda = Soda(user_input)
