with open("students.txt", "w", encoding="utf-8") as f:
    f.write("Иванов Иван:5,4,3,5\n")
    f.write("Петров Петр:4,3,4,4\n")
    f.write("Сидорова Мария:5,5,5,5\n")

print("--- Содержимое файла students.txt ---")
with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read().strip())

best_student = ""
max_score = 0
filtered_students = []

print("\n--- Расчет среднего балла для каждого ---")
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line: continue

        name, grades_str = line.split(":")
        grades = [int(g) for g in grades_str.split(",")]

        avg = sum(grades) / len(grades)
        print(f"{name}: {avg:.2f}")

        if avg > 4.0:
            filtered_students.append(f"{name}:{avg:.2f}\n")

        if avg > max_score:
            max_score = avg
            best_student = name

with open("result.txt", "w", encoding="utf-8") as out:
    out.writelines(filtered_students)

print("\n--- Студенты в файле result.txt (балл > 4.0) ---")
with open("result.txt", "r", encoding="utf-8") as res_file:
    print(res_file.read().strip())

print("\n--- Итог ---")
print(f"Студент с наивысшим баллом: {best_student} ({max_score:.2f})")