# Паттерн «Фабричный метод»
# ● Создайте абстрактный класс Animal, у которого есть абстрактный метод speak.
# ● Создайте классы Dog и Cat, которые наследуют от Animal и реализуют метод speak.
# ● Создайте класс AnimalFactory, который использует паттерн «Фабричный метод» для создания экземпляра Animal.
# Этот класс должен иметь метод create_animal, который принимает строку («dog» или «cat») и возвращает соответствующий
# объект (Dog или Cat).
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class AnimalFactory:
    def create_animal(self, animal_type: str):
        try:
            if animal_type.lower() == "dog":
                return Dog()
            elif animal_type.lower() == "cat":
                return Cat()
            else:
                raise ValueError(f"Неизвестный тип животного: {animal_type}")
        except Exception as e:
            print(f"Ошибка при создании животного: {e}")
            return None


if __name__ == "__main__":
    factory = AnimalFactory()

    dog = factory.create_animal("dog")
    if dog:
        print("Собака говорит:", dog.speak())

    cat = factory.create_animal("cat")
    if cat:
        print("Кошка говорит:", cat.speak())

    unicorn = factory.create_animal("unicorn")
    if unicorn:
        print(unicorn.speak())
