import csv

initial_data = [
    ["Название", "Цена", "Количество"],
    ["Яблоки", 100, 50],
    ["Бананы", 80, 30],
    ["Молоко", 120, 20],
    ["Хлеб", 40, 100]
]

filename = 'products.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(initial_data)


def load_data():
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Преобразуем числа из строк обратно в int
                row['Цена'] = int(row['Цена'])
                row['Количество'] = int(row['Количество'])
                products.append(row)
    except FileNotFoundError:
        print("Файл не найден.")
    return products


def save_data(products):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Название", "Цена", "Количество"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    print("Данные успешно сохранены.")


def main():
    products = load_data()

    while True:
        print("\n--- Меню управления складом ---")
        print("1. Показать все товары")
        print("2. Добавить новый товар")
        print("3. Поиск товара по названию")
        print("4. Рассчитать общую стоимость склада")
        print("5. Сохранить изменения и выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            for p in products:
                print(f"{p['Название']}: {p['Цена']} руб., {p['Количество']} шт.")

        elif choice == '2':
            name = input("Введите название: ")
            price = int(input("Введите цену: "))
            qty = int(input("Введите количество: "))
            products.append({"Название": name, "Цена": price, "Количество": qty})
            print("Товар добавлен в список.")

        elif choice == '3':
            search_name = input("Что ищем? ").lower()
            found = [p for p in products if search_name in p['Название'].lower()]
            if found:
                for p in found:
                    print(f"Найдено: {p['Название']} — {p['Цена']} руб., {p['Количество']} шт.")
            else:
                print("Товар не найден.")

        elif choice == '4':
            total = sum(p['Цена'] * p['Количество'] for p in products)
            print(f"Общая стоимость всех товаров на складе: {total} руб.")

        elif choice == '5':
            save_data(products)
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()