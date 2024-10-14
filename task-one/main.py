import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Робить копію файлів зі вказаної директорії і сортує по розширенню файлу.")
    parser.add_argument("source_dir", help="Шлях до оригінальної директорії.")
    parser.add_argument("destination_dir", nargs='?', default="dist", help="Шлях до директорії призначення. За замовченням 'dist'.")
    return parser.parse_args()

def copy_and_sort_files(source_dir, destination_dir):
    # Створює директорію призначення, якщо не існує
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
	# Рекрусивно проходить по всім елементам початкової директорії
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        if os.path.isdir(source_item):

            copy_and_sort_files(source_item, destination_dir)
        elif os.path.isfile(source_item):
            try:

                file_extension = os.path.splitext(item)[1].lstrip(".").lower()
                if not file_extension:
                    file_extension = "no_extension"
                destination_path = os.path.join(destination_dir, file_extension)
                
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
					
                shutil.copy2(source_item, destination_path)
            except Exception as e:
                print(f"Помилка копіювання {source_item}: {e}")

def main():
	# Парсить аргументи командного рядка
    args = parse_arguments()
    source_dir = args.source_dir
    destination_dir = args.destination_dir
	
	# Перевіряє чи існує оригінальна директорія
    if not os.path.exists(source_dir):
        print(f"Директорія '{source_dir}' не існує.")
        return

	# Розпочинає процес копіювання і сортування файлів
    copy_and_sort_files(source_dir, destination_dir)
    print(f"Файли були скопійовані в '{destination_dir}'")

if __name__ == "__main__":
    main()
