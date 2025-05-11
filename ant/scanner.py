import os
import yara 

# Загрузка правил из файла malware.yar
rules = yara.compile(filepath='malware.yar') 

def scan_file(filepath):
    try:
        matches = rules.match(filepath)
        if matches:
            print(f"Вирус обнаружен в файле: {filepath}")
            print("Найденные правила:")
            for match in matches:
                print(f" - {match.rule}")
            action = input("Удалить файл? (y/n): ").lower()
            if action == 'y':
                os.remove(filepath)
                print(f"Файл {filepath} удалён.")
            else:
                print("Файл не удалён.")
            return True
        else:
            print("Вирусов нет! Ура победа с 9 мая всех!!!")
    except Exception as e:

        print(f"Ошибка при сканировании {filepath}: {e}")
    return False

def scan_directory(directory):
    try:
        for root, _, files in os.walk(directory):
            for filename in files:
                print(filename)
                filepath = os.path.join(root, filename)
                scan_file(filepath)
    except Exception as e:
        print(f"Ошибка: {e}")

path = input("Введите путь для сканирования: ")
scan_directory(path)