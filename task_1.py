filename = "text.txt"

print("Введите 5 строк текста:")
with open(filename, "w", encoding="utf-8") as file:
    for i in range(5):
        line = input(f"Строка {i+1}: ")
        file.write(line + "\n")

with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

num_lines = len(lines)

all_text = "".join(lines)
words = all_text.split()
num_words = len(words)

longest_line = max(lines, key=lambda s: len(s.strip()))

print("\n--- Результаты анализа ---")
print(f"Количество строк: {num_lines}")
print(f"Количество слов: {num_words}")
print(f"Самая длинная строка: {longest_line.strip()}")