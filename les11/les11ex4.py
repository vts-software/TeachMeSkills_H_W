# Программа с классом Sphere для представления сферы
# в трёхмерном пространстве
import math  # Подключаем модуль math, в нём есть число pi и другие полезные функции.

class Sphere:

    def __init__(self, radius=1, x=0.0, y=0.0, z=0.0):

        if radius < 0:

            raise ValueError("Радиус не может быть отрицательным")
        self._radius = float(radius)
        self._center = (float(x), float(y), float(z))

    def get_volume(self):
        return 4.0/3.0 * math.pi * self._radius**3

    def get_square(self):
        return 4.0 * math.pi * self._radius**2

    def get_radius(self):
        return self._radius

    def get_center(self):
        return self._center

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self._radius = float(radius)

    def set_center(self, x, y, z):
        self._center = (float(x), float(y), float(z))

    def is_point_inside(self, x, y, z):
        dx = x - self._center[0]
        dy = y - self._center[1]
        dz = z - self._center[2]
        dist_sq = dx*dx + dy*dy + dz*dz
        return dist_sq <= self._radius * self._radius

    def __repr__(self):
        return f"Sphere(radius={self._radius}, center={self._center})"



try:
    radius = float(input("Введите радиус сферы (или оставьте пустым для 1): ") or 1)
    x = float(input("Введите координату X центра (или пусто для 0): ") or 0)
    y = float(input("Введите координату Y центра (или пусто для 0): ") or 0)
    z = float(input("Введите координату Z центра (или пусто для 0): ") or 0)

    sphere = Sphere(radius, x, y, z)

    print("\nСоздана сфера:", sphere)
    print(f"Объём: {sphere.get_volume():.4f}")
    print(f"Площадь поверхности: {sphere.get_square():.4f}")

    px = float(input("\nВведите X точки: "))
    py = float(input("Введите Y точки: "))
    pz = float(input("Введите Z точки: "))

    inside = sphere.is_point_inside(px, py, pz)
    if inside:
        print("Точка находится ВНУТРИ сферы.")
    else:
        print("Точка находится СНАРУЖИ сферы.")

except ValueError as e:
    print("Ошибка ввода:", e)
