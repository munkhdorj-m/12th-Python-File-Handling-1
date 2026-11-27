# Python File Handling with Exception Handling 1
 
Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

Python Exception handling
https://drive.google.com/file/d/1JaPWKbfL4jOw8IPTJo67dFypR-BhDm3t/view?usp=sharing

**Rules for this assignment**

- **Every** function must use exception handling (`try` / `except`). A test
  checks for it.
- Do not let your program crash — catch the error and do what the exercise says.
- Functions **return** their answer. Only print the messages the exercise asks for.
- Always **close** a file when you have finished with it.


## Before you start: exceptions

An **exception** is an error that happens while the program is **running**
(not a syntax error). If nothing catches it, the program crashes.

    Number = int("abc")      →  ValueError: invalid literal for int()
    File = open("x.txt")     →  FileNotFoundError: No such file or directory

**Exception handling** means: *try* the risky code, and if an exception
happens, *jump* to code that deals with it — instead of crashing.

    try:
        File = open("scores.txt", "r")
    except FileNotFoundError:
        print("File not found")

- The code in `try:` runs first.
- If an exception happens, Python **stops** the `try:` part at that line and
  runs the matching `except:` part.
- If no exception happens, the `except:` part is skipped.

Put the `try` **inside** the loop. A bad line is caught, and the loop carries on
with the next line:

    for Line in File:
        try:
            Number = int(Line.strip())
            Total = Total + Number
        except ValueError:
            print("Bad line skipped")

---

## Exercise 1

**Problem:**

`ReadNumbers(FileName)`

The file holds one value on each line. Most lines are whole numbers, but some
are not (words, decimals, empty lines).

- Return a **list** of all the whole numbers in the file, in the same order
- **Skip** any line that is not a whole number — do not crash
- If the file does not exist, output `File not found` and return `[]`

Negative numbers like `-2` **are** whole numbers. (So `.isdigit()` is not good
enough — use `try` / `except ValueError`.)

**Example:**

`numbers.txt` contains:

    5
    abc

    3.5
    8
    -2

    Input:
      print(ReadNumbers("numbers.txt"))
      print(ReadNumbers("missing.txt"))

    Output:
      [5, 8, -2]
      File not found
      []

---

## Exercise 2

**Problem:**

`WriteScores(FileName, Scores)`

`Scores` is a 2D list. Each item is `[Name, Score]`.

- Write each student to the file on its own line as `Name,Score`
- Any old contents of the file are **replaced**
- Return `True` if the file was written
- If the file cannot be opened for writing, output `Cannot write to file`
  and return `False`

A file cannot be opened for writing when its **folder does not exist**, or when
the name is a **folder**, not a file. These raise **different** exceptions — so
catch `OSError` (or `IOError`), which covers **all** file problems.

**Example:**

    Input:
      print(WriteScores("scores.txt", [["Anu", 85], ["Bat", 62]]))
      print(WriteScores("no_folder/scores.txt", [["Anu", 85]]))

    Output:
      True
      Cannot write to file
      False

`scores.txt` now contains:

    Anu,85
    Bat,62

---

## Exercise 3

**Problem:**

`ProcessResults(InFile, OutFile)`

`InFile` holds exam results, one student per line: `Name,Score`.

For each **valid** line, write `Name,Grade` to `OutFile`:

| Score | Grade |
|---|---|
| 80 – 100 | A |
| 60 – 79 | B |
| 40 – 59 | C |
| 0 – 39 | U |

A line is **invalid** if:

- it does not have exactly **one** comma (`Bat` or `Zaya,50,70`)
- the score is not a whole number (`Tom,abc` or `Dorj,7.5`)
- the score is less than 0 or more than 100 (`Saraa,105`)

Invalid lines are **not** written to `OutFile`. Count them, and return the
number of invalid lines.

If `InFile` does not exist, output `File not found` and return `-1`.

*Hint:* `try` / `except ValueError` catches a score that is not a whole number.
The comma check and the 0–100 check are normal `if` statements — count those
lines as invalid too.

**Example:**

`results.txt` contains:

    Anu,85
    Bat
    Tom,abc
    Saraa,105
    Nomin,60

    Input:
      print(ProcessResults("results.txt", "grades.txt"))

    Output:
      3

`grades.txt` now contains:

    Anu,A
    Nomin,B

---
