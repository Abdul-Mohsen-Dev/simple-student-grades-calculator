# Student Grades Calculator

A very simple Python program for teachers. You type each student's grade, and it shows the average, the highest and lowest grades, and how many students passed or failed.

## Requirements

- Python 3 installed on your computer

## How to run

Open a terminal in the project folder and run:

```
python3 grades.py
```

On Windows, use `python grades.py`.

## How to use

1. Type a student's grade and press Enter.
2. Repeat for every student.
3. Type `done` when you finish.

Grades must be numbers between 0 and 100. Anything else is rejected and the program asks again.

## Example

```
Type each student's grade and press Enter. Type 'done' when finished.
Grade: 80
Grade: 45
Grade: 60
Grade: done

Students: 3
Average: 61.67
Highest: 80.0
Lowest: 45.0
Passed: 2
Failed: 1
```

## Settings

The passing grade is 50. To change it, edit this line in `grades.py`:

```python
PASS_MARK = 50
```
