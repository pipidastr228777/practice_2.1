import json
import os

FILENAME = "library.json"


def load_data():
    if not os.path.exists(FILENAME):
        initial_data = [
            {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "available": True},
            {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "available": False}
        ]
        save_data(initial_data)
        return initial_data

    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def show_books(books):
    print("\n--- Список книг ---")
    for b in books:
        status = "В наличии" if b['available'] else "Выдана"
        print(f"ID: {b['id']} | '{b['title']}' ({b['author']}) | Год: {b['year']} | Статус: {status}")


def main():
    library = load_data()

    while True:
        print("\nМеню библиотеки:")
        print("1. Просмотр всех книг")
        print("2. Поиск по автору/названию")
        print("3. Добавление новой книги")
        print("4. Изменить статус (взята/возвращена)")
        print("5. Удаление книги по ID")
        print("6. Экспорт доступных книг в .txt")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            show_books(library)

        elif choice == "2":
            query = input("Введите название или автора: ").lower()
            results = [b for b in library if query in b['title'].lower() or query in b['author'].lower()]
            show_books(results) if results else print("Ничего не найдено.")

        elif choice == "3":
            new_id = max([b['id'] for b in library], default=0) + 1
            title = input("Название: ")
            author = input("Автор: ")
            year = int(input("Год издания: "))
            library.append({"id": new_id, "title": title, "author": author, "year": year, "available": True})
            save_data(library)
            print("Книга добавлена!")

        elif choice == "4":
            book_id = int(input("Введите ID книги для смены статуса: "))
            for b in library:
                if b['id'] == book_id:
                    b['available'] = not b['available']
                    save_data(library)
                    print(f"Статус изменен! Теперь: {'В наличии' if b['available'] else 'Выдана'}")
                    break
            else:
                print("Книга с таким ID не найдена.")

        elif choice == "5":
            book_id = int(input("Введите ID для удаления: "))
            library = [b for b in library if b['id'] != book_id]
            save_data(library)
            print("Данные обновлены.")

        elif choice == "6":
            available_ones = [f"{b['title']} — {b['author']}" for b in library if b['available']]
            with open("available_books.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(available_ones))
            print(f"Экспортировано {len(available_ones)} книг в available_books.txt")

        elif choice == "0":
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
