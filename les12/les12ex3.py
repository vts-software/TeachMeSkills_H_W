# Сокращённый вид класса (как в демонстрации)
import math

class Bus:

    def __init__(self, max_seats, max_speed):

        if max_seats <= 0:
            raise ValueError("max_seats должен быть положительным")

        if max_speed < 0:
            raise ValueError("max_speed не может быть отрицательной")

        self.max_seats = int(max_seats)
        self.max_speed = float(max_speed)
        self.speed = 0.0
        self.passengers = []
        self.has_free_seats = True
        self.seat_map = {i: None for i in range(1, self.max_seats + 1)}

    def _update_free_seats(self):
        self.has_free_seats = any(v is None for v in self.seat_map.values())

    def board(self, names):

        if self.speed > 0:
            raise RuntimeError("Нельзя сажать пассажиров на ходу. Сначала остановите автобус (speed = 0).")

        if isinstance(names, str):
            names = [names]
        seated = []
        not_seated = []

        for name in names:
            free_seat = None

            for seat, occupant in self.seat_map.items():

                if occupant is None:
                    free_seat = seat
                    break

            if free_seat is None:
                not_seated.append(name)

            else:
                self.seat_map[free_seat] = name
                self.passengers.append(name)
                seated.append((name, free_seat))
        self._update_free_seats()

        return seated, not_seated

    def alight(self, names):

        if self.speed > 0:
            raise RuntimeError("Нельзя высаживать пассажиров на ходу. Сначала остановите автобус (speed = 0).")

        if isinstance(names, str):
            names = [names]
        removed = []
        not_found = []

        for name in names:
            found_seat = None

            for seat, occupant in self.seat_map.items():

                if occupant == name:
                    found_seat = seat
                    break

            if found_seat is None:
                not_found.append(name)

            else:
                self.seat_map[found_seat] = None

                try:
                    self.passengers.remove(name)

                except ValueError:
                    pass

                removed.append((name, found_seat))

        self._update_free_seats()

        return removed, not_found

    def change_speed(self, delta):
        new_speed = self.speed + float(delta)

        if new_speed < 0:
            new_speed = 0.0

        if new_speed > self.max_speed:
            new_speed = self.max_speed
        self.speed = new_speed

        return self.speed

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, other):
        self.board(other)

        return self

    def __isub__(self, other):
        self.alight(other)

        return self

    def __repr__(self):

        return (f"Bus(speed={self.speed}, seats={self.max_seats}, "
                f"passengers={len(self.passengers)})")


# Простая командная логика, которая подсказывает последовательность:
if __name__ == "__main__":
    max_seats = int(input("Введите количество мест в автобусе: "))
    max_speed = float(input("Введите максимальную скорость автобуса: "))
    bus = Bus(max_seats, max_speed)

    print("\nСценарий: сначала посадка, затем движение (speed>0), затем остановка (speed=0), затем высадка и новая посадка.")

    while True:
        print("\nДоступные команды:")
        print("  1  - посадить (только когда speed == 0)")
        print("  2 - высадить (только когда speed == 0)")
        print("  3  - изменить скорость (+/- число)")
        print("  4  - показать состояние автобуса")
        print("  0   - выйти")
        cmd = input("Команда: ").strip().lower()

        if cmd == "0":
            print("Выход.")
            break

        elif cmd == "1":
            names = input("Фамилии через запятую: ").strip()
            names = [n.strip() for n in names.split(",") if n.strip()]

            try:
                seated, not_seated = bus.board(names)
                print("Посадили:", seated)
                print("Не смогли сесть:", not_seated)

            except RuntimeError as e:
                print("Ошибка:", e)

        elif cmd == "2":
            names = input("Фамилии через запятую: ").strip()
            names = [n.strip() for n in names.split(",") if n.strip()]

            try:
                removed, not_found = bus.alight(names)
                print("Высажены:", removed)
                print("Не найдены:", not_found)

            except RuntimeError as e:
                print("Ошибка:", e)

        elif cmd == "3":
            delta = float(input("Введите изменение скорости (+ или - число): "))
            old_speed = bus.speed
            new_speed = bus.change_speed(delta)
            print(f"Скорость была {old_speed}, теперь {new_speed}")

            if old_speed == 0 and new_speed > 0:
                print("Автобус поехал — теперь посадка/высадка запрещены до остановки.")

            if old_speed > 0 and new_speed == 0:
                print("Автобус остановлен — теперь можно высаживать/садить пассажиров.")

        elif cmd == "4":
            print(bus)
            print("Места:", bus.seat_map)
            print("Пассажиры:", bus.passengers)

        else:
            print("Неизвестная команда. Введите одну из перечисленных.")

