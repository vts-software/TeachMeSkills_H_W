# В текстовый файл построчно записаны фамилия и имя
# учащихся класса и оценка за контрольную. Вывести на экран
# всех учащихся, чья оценка меньше трёх баллов.

# Функция, которая очищает токен с оценкой и делает десятичную точку одинокой
def clean_grade_token(token):
    token = token.strip()                      # убрать пробелы по краям
    token = token.strip(".,;:()\"'")           # убрать знаки пунктуации по краям
    token = token.replace(",", ".")            # заменить запятую на точку (2,5 -> 2.5)
    return token

# Основная функция: читает входной файл и (по желанию) пишет файл с двоечниками
def find_failing_students(input_path="students.txt",
                          output_path=None,
                          threshold=3.0):
    failing = []  # сюда будем собирать (ФИО, оценка, номер строки)

    # Открываем входной файл построчно
    with open(input_path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):   # lineno — номер текущей строки (1,2,3...)
            original_line = line           # сохраняем оригинал для сообщений
            line = line.strip()            # убрать пробелы и переносы по краям

            if not line:
                continue

            parts = line.split()

            if len(parts) < 2:
                print(f"Пропущена строка {lineno}: недостаточно данных -> {original_line!r}")
                continue

            raw_grade = parts[-1] # предполагаем: последняя часть — оценка
            grade_str = clean_grade_token(raw_grade)

            try:
                grade = float(grade_str)   # пробуем превратить в число (поддерживает 2 и 2.5)

            except ValueError:
                print(f"Пропущена строка {lineno}: нельзя прочитать оценку '{raw_grade}'")
                continue

            surname = parts[0]   # первая часть — фамилия
            name = " ".join(parts[1:-1]) if len(parts) > 2 else ""  # всё между фамилией и оценкой — имя/отчество

            # Если оценка меньше порога — добавляем в список двоечников
            if grade < threshold:
                full_name = f"{surname} {name}".strip()  # собрать имя, убрать лишние пробелы
                failing.append((full_name, grade, lineno))

    # Выводим двоечников на экран
    if failing:
        print("Учащиеся с оценкой ниже 3:")
        for full_name, grade, lineno in failing:
            print(f"{full_name} — {grade} (строка {lineno})")
    else:
        print("Учащихся с оценкой ниже 3 не найдено.")

    # По желанию записываем результат в файл
    if output_path:
        with open(output_path, "w", encoding="utf-8") as out:
            for full_name, grade, lineno in failing:
                out.write(f"{full_name} {grade}\n")


if __name__ == "__main__":
    # пример: прочитать students.txt и записать двоечников в failing_students.txt
    find_failing_students("students.txt", output_path="failing_students.txt")
