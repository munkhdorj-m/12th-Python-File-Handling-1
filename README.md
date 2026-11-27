# Python File Handling with Exception Handling 1
 
Python File handling
https://drive.google.com/file/d/1sIv9rb6PizW9sfts9eVu0BkLYWLjysiT/view

Python Exception handling
https://drive.google.com/file/d/1JaPWKbfL4jOw8IPTJo67dFypR-BhDm3t/view?usp=sharing

**Rules for this assignment**

- **Every** function must use exception handling (`try` / `except`). A test
  checks for it.
- Your program must **never crash** — catch the error and do what the exercise says.
- Functions **return** their answer. Only print the messages the exercise asks for.
- Always **close** a file when you have finished with it.


## Before you start: exceptions

An **exception** is an error that happens while the program is **running**.
If nothing catches it, the program **crashes**.

    File = open("missing.txt", "r")    →  FileNotFoundError
    Number = int("hello")              →  ValueError

**Exception handling** means: *try* the risky code. If an exception happens,
Python jumps to the `except` part instead of crashing.

    try:
        File = open("data.txt", "r")
        print(File.read())
        File.close()
    except FileNotFoundError:
        print("File not found")

- The code in `try:` runs first.
- If an exception happens, Python **stops** the `try:` part at that line and
  runs the matching `except:` part.
- If no exception happens, the `except:` part is skipped.

**More than one `except`**

One `try` can have several `except` blocks — one for each kind of error.
Python runs the one that matches:

    try:
        Age = int(input("Age: "))
        print(100 / Age)
    except ValueError:
        print("That is not a whole number")
    except ZeroDivisionError:
        print("Age cannot be 0")

**Exceptions you need today**

| Exception | When it happens |
|---|---|
| `FileNotFoundError` | Opening a file for **reading** that does not exist |
| `OSError` (also called `IOError`) | **Any** file problem — including a file that cannot be written |
| `ValueError` | `int("hello")`, `int("3.5")`, `int("")` |

---

## Exercise 1

**Problem:**

`ReadFile(FileName)`

- Return **all** the text in the file as one string
- If the file does not exist, output `File not found` and return `""`

**Example:**

`hello.txt` contains:

    Hello
    World

    Input:
      print(ReadFile("hello.txt"))
      print(ReadFile("missing.txt"))

    Output:
      Hello
      World

      File not found

---

## Exercise 2

**Problem:**

`ReadNumber(FileName)`

The **first line** of the file should hold a whole number.

- Return that number as an **integer**
- If the file does not exist, output `File not found` and return `-1`
- If the first line is not a whole number, output `Not a number` and return `-1`

You need **two** `except` blocks — one for each error.

*Hint:* `File.readline()` reads one line. Use `.strip()` before `int()`.

**Example:**

`number.txt` contains `42`. `word.txt` contains `hello`.

    Input:
      print(ReadNumber("number.txt"))
      print(ReadNumber("missing.txt"))
      print(ReadNumber("word.txt"))

    Output:
      42
      File not found
      -1
      Not a number
      -1

---

## Exercise 3

**Problem:**

`SaveMessage(FileName, Message)`

- Write `Message` to the file (replace anything already in it)
- Return `True`
- If the file cannot be written, output `Cannot save` and return `False`

A file cannot be written when, for example, its **folder does not exist**.
Catch `OSError` (or `IOError`) — it covers **every** file problem.

**Example:**

    Input:
      print(SaveMessage("message.txt", "Hello class"))
      print(SaveMessage("no_folder/message.txt", "Hello"))

    Output:
      True
      Cannot save
      False

`message.txt` now contains:

    Hello class

---

## Exercise 4

**Problem:**

`TotalOfFile(FileName)`

The file holds one value on each line. Most are whole numbers, but some are not.

- Return the **total** of all the whole numbers in the file
- **Skip** any line that is not a whole number — do not stop
- If the file does not exist, output `File not found` and return `-1`

*Hint:* put a **second** `try` / `except ValueError` **inside** the loop.
Then a bad line is skipped and the loop carries on with the next line.

**Example:**

`numbers.txt` contains:

    10
    ten

    2.5
    20

    Input:
      print(TotalOfFile("numbers.txt"))
      print(TotalOfFile("missing.txt"))

    Output:
      30
      File not found
      -1

---

