# Student Grades Calculator - a very simple Python project
# Enter each student's grade and the program shows the average,
# highest, lowest, and how many passed.

PASS_MARK = 50  # passing grade, change it if you want

grades = []

print("Type each student's grade and press Enter. Type 'done' when finished.")

while True:
    text = input("Grade: ").strip()
    if text.lower() == "done":
        break
    try:
        grade = float(text)
    except ValueError:
        print("Please type a number, or 'done' to finish.")
        continue
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        continue
    grades.append(grade)

if not grades:
    print("No grades were entered.")
else:
    passed = len([g for g in grades if g >= PASS_MARK])
    print()
    print("Students:", len(grades))
    print("Average:", round(sum(grades) / len(grades), 2))
    print("Highest:", max(grades))
    print("Lowest:", min(grades))
    print("Passed:", passed)
    print("Failed:", len(grades) - passed)