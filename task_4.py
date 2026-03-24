from datetime import datetime
import os

LOG_FILE = "calculator.log"


def show_last_logs():
    if os.path.exists(LOG_FILE):
        print("\n--- Последние 5 операций ---")
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[-5:]:
                print(line.strip())
    else:
        print("\nИстория операций пока пуста.")


def clear_log():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        pass
    print("Лог-файл успешно очищен.")


def main():
    show_last_logs()

    while True:
        print("\n--- Меню калькулятора ---")
        print("Доступные действия: +, -, *, /")
        print("Команды: 'clear' — очистить лог, 'exit' — выход")

        user_input = input("Введите операцию или команду: ").lower()

        if user_input == 'exit':
            break
        elif user_input == 'clear':
            clear_log()
            continue
        elif user_input not in ['+', '-', '*', '/']:
            print("Ошибка: Неизвестная операция.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            result = None
            if user_input == '+':
                result = num1 + num2
            elif user_input == '-':
                result = num1 - num2
            elif user_input == '*':
                result = num1 * num2
            elif user_input == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль!")
                    continue
                result = num1 / num2

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {num1} {user_input} {num2} = {result}"

            print(f"Результат: {result}")

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")

        except ValueError:
            print("Ошибка: Введите корректные числа.")


if __name__ == "__main__":
    main()
