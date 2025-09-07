# 8. JSON и CSV.
# Исходные данные:
# https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2Xn
# JDv9xN2LxusbE?usp=sharing
import json
import csv


def json_to_csv(json_file="employees.json", csv_file="employees.csv"):
    # Читаем JSON
    with open(json_file, "r", encoding="utf-8") as f:
        employees = json.load(f)

    # Определяем поля CSV (заголовки)
    # Допустим: name, birth_year, height, languages (языки — строка через запятую)
    fieldnames = ["name", "birth_year", "height", "languages"]

    # Записываем в CSV
    with open(csv_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for emp in employees:
            row = {
                "name": emp.get("name", ""),
                "birth_year": emp.get("birth_year", ""),
                "height": emp.get("height", ""),
                "languages": ", ".join(emp.get("languages", []))
            }

            writer.writerow(row)


# функция добавления нового сотрудника
def add_employee_to_json(json_file="employees.json"):
    # Читаем текущие данные
    try:

        with open(json_file, "r", encoding="utf-8") as f:
            employees = json.load(f)

    except FileNotFoundError:
        employees = []

    # Ввод данных
    name = input("Введите имя сотрудника: ")
    birth_year = int(input("Введите год рождения: "))
    height = int(input("Введите рост (см): "))
    languages_str = input("Введите языки программирования через запятую: ")
    languages = [lang.strip() for lang in languages_str.split(",") if lang.strip()]

    # Создаём новую запись
    new_employee = {
        "name": name,
        "birth_year": birth_year,
        "height": height,
        "languages": languages
    }

    # Добавляем и сохраняем
    employees.append(new_employee)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)
    print("Сотрудник добавлен в JSON файл.")


# функция добавления сотрудника в CSV
def add_employee_to_csv(csv_file="employees.csv"):
    name = input("Введите имя сотрудника: ")
    birth_year = input("Введите год рождения: ")
    height = input("Введите рост (см): ")
    languages_str = input("Введите языки программирования через запятую: ")

    with open(csv_file, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, birth_year, height, languages_str])
    print("Сотрудник добавлен в CSV файл.")


# Функция вывода информации о сотруднике по имени
def find_employee_by_name(json_file="employees.json"):
    name_search = input("Введите имя для поиска: ").lower()

    with open(json_file, "r", encoding="utf-8") as f:
        employees = json.load(f)

    found = False

    for emp in employees:

        if name_search in emp.get("name", "").lower():
            print(f"Имя: {emp.get('name')}")
            print(f"Год рождения: {emp.get('birth_year')}")
            print(f"Рост: {emp.get('height')} см")
            print(f"Языки: {', '.join(emp.get('languages', []))}")
            print("-" * 20)
            found = True


    if not found:
        print("Сотрудник не найден.")


# Фильтр по языку программирования
def filter_by_language(json_file="employees.json"):
    lang_search = input("Введите язык программирования для фильтра: ").lower()

    with open(json_file, "r", encoding="utf-8") as f:
        employees = json.load(f)

    filtered = [emp for emp in employees if any(lang_search == lang.lower() for lang in emp.get("languages", []))]

    if filtered:
        print(f"Сотрудники, владеющие {lang_search}:")

        for emp in filtered:
            print(emp.get("name"))

    else:
        print(f"Сотрудники, владеющие {lang_search}, не найдены.")


# Фильтр по году рождения и вывод среднего роста
def average_height_by_birth_year(json_file="employees.json"):
    year_limit = int(input("Введите год рождения: "))

    with open(json_file, "r", encoding="utf-8") as f:
        employees = json.load(f)

    filtered = [emp for emp in employees if emp.get("birth_year", 9999) < year_limit]


    if not filtered:
        print("Сотрудников с годом рождения меньше заданного не найдено.")
        return

    total_height = sum(emp.get("height", 0) for emp in filtered)
    avg_height = total_height / len(filtered)
    print(f"Средний рост сотрудников, родившихся до {year_limit}: {avg_height:.2f} см")


# Интерактивное меню
def menu():

    while True:
        print("\nМеню:")
        print("1. Конвертировать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Фильтр по году рождения (средний рост)")
        print("0. Выход")

        choice = input("Выберите действие: ")


        if choice == "1":
            json_to_csv()

        elif choice == "2":
            add_employee_to_json()

        elif choice == "3":
            add_employee_to_csv()

        elif choice == "4":
            find_employee_by_name()

        elif choice == "5":
            filter_by_language()

        elif choice == "6":
            average_height_by_birth_year()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()
