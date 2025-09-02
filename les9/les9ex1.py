
import os #работа с файлами и папками на компьютере.
import shutil #позволяет перемещать и переименовывать файлы
from collections import defaultdict #словарь, который создаёт список, если мы обращаемся к ключу впервые.


#создаем функцию которая отображает имя ОС
# текущий путь
# расширение файла
def sort_files_by_extension(folder_path):
    os_name = os.name

    if os_name == "nt":
        print("Операционная система: Windows")

    elif os.name == "posix":

        print("Вы работаете в Unix-подобной системе (macOS, Linux, etc.)")

    else:

        print("Неизвестная операционная система")

    # текущее расположение. Превращаем относительный путь в полный.
    current_path = os.path.abspath(folder_path)
    print(f"Текущий путь: {current_path}")

    # Создаем словарь: расширение -> список файлов с этим расширением
    files_by_ext = defaultdict(list)


        # Сканируем папку
    for filename in os.listdir(current_path):
        filepath = os.path.join(current_path, filename)

        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1]
            files_by_ext[ext].append(filename)


        # Для каждого расширения — своя папка
    for ext, files in files_by_ext.items():

        if not ext:

            continue  # Пропустить файлы без расширения

        folder_name = ext[1:] + "_files"  # на выходе .txt → txt_files
        new_folder_path = os.path.join(current_path, folder_name)
        os.makedirs(new_folder_path, exist_ok = True) #создаем папку, если ее нет. Если есть, то питон не будеть ругаться

        total_size = 0  # Общий размер файлов


            # Перемещаем файлы в новую папку
        for filename in files:
            src = os.path.join(current_path, filename) #откуда берем файлы
            dst = os.path.join(new_folder_path, filename) #сюда переместим
            shutil.move(src, dst) # перемещаем из старой папки в новую
            total_size += os.path.getsize(dst) #Прибавляем размер файла в общий счётчик.

            # Переводим байты в мб
        size_mb = total_size / (1024 * 1024)
        print(f"В папку {folder_name} перемещено {len(files)} файлов, их суммарный размер — {size_mb:.2f} МБ")

            # Переименовываем один файл
        if files:
            old_name = files[0]
            new_name = "new_" + old_name
            old_path = os.path.join(new_folder_path, old_name)
            new_path = os.path.join(new_folder_path, new_name)
            os.rename(old_path, new_path) #Переименовываем файл
            print(f"Файл {old_name} был переименован в {new_name}")


if __name__ == "__main__":
    folder = input("Введите путь к папке, которую нужно обработать: ")
    sort_files_by_extension(folder)