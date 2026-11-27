import ast
import inspect
import textwrap

import pytest

import assignment


def uses_try(function):
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            return True
    return False


def make_file(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text)
    return str(path)


def read_file(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text


def test1_read_file(tmp_path):
    path = make_file(tmp_path, "hello.txt", "Hello\nWorld\n")
    assert assignment.ReadFile(path) == "Hello\nWorld\n"
    path = make_file(tmp_path, "empty.txt", "")
    assert assignment.ReadFile(path) == ""


def test1_file_not_found(tmp_path, capsys):
    assert assignment.ReadFile(str(tmp_path / "missing.txt")) == ""
    assert capsys.readouterr().out == "File not found\n"
    assert uses_try(assignment.ReadFile), "ReadFile() must use try / except."


def test2_read_number(tmp_path):
    path = make_file(tmp_path, "number.txt", "42\n")
    assert assignment.ReadNumber(path) == 42
    path = make_file(tmp_path, "negative.txt", "-7")
    assert assignment.ReadNumber(path) == -7


def test2_file_not_found(tmp_path, capsys):
    assert assignment.ReadNumber(str(tmp_path / "missing.txt")) == -1
    assert capsys.readouterr().out == "File not found\n"
    assert uses_try(assignment.ReadNumber), "ReadNumber() must use try / except."


def test2_not_a_number(tmp_path, capsys):
    path = make_file(tmp_path, "word.txt", "hello\n")
    assert assignment.ReadNumber(path) == -1
    assert capsys.readouterr().out == "Not a number\n"
    path = make_file(tmp_path, "decimal.txt", "3.5\n")
    assert assignment.ReadNumber(path) == -1
    assert capsys.readouterr().out == "Not a number\n"
    path = make_file(tmp_path, "empty.txt", "")
    assert assignment.ReadNumber(path) == -1
    assert capsys.readouterr().out == "Not a number\n"


def test3_save_message(tmp_path):
    path = str(tmp_path / "message.txt")
    assert assignment.SaveMessage(path, "Hello class") == True
    assert read_file(path) == "Hello class"


def test3_replaces_old_message(tmp_path):
    path = make_file(tmp_path, "message.txt", "Old message")
    assert assignment.SaveMessage(path, "New") == True
    assert read_file(path) == "New"


def test3_cannot_save(tmp_path, capsys):
    path = str(tmp_path / "no_folder" / "message.txt")
    assert assignment.SaveMessage(path, "Hello") == False
    assert capsys.readouterr().out == "Cannot save\n"
    assert assignment.SaveMessage(str(tmp_path), "Hello") == False
    assert capsys.readouterr().out == "Cannot save\n"
    assert uses_try(assignment.SaveMessage), "SaveMessage() must use try / except."


def test4_total(tmp_path):
    path = make_file(tmp_path, "numbers.txt", "10\n20\n5\n-3\n")
    assert assignment.TotalOfFile(path) == 32
    path = make_file(tmp_path, "empty.txt", "")
    assert assignment.TotalOfFile(path) == 0


def test4_skips_bad_lines(tmp_path):
    path = make_file(tmp_path, "numbers.txt", "10\nten\n\n2.5\n20\n")
    assert assignment.TotalOfFile(path) == 30
    path = make_file(tmp_path, "words.txt", "a\nb\n")
    assert assignment.TotalOfFile(path) == 0


def test4_file_not_found(tmp_path, capsys):
    assert assignment.TotalOfFile(str(tmp_path / "missing.txt")) == -1
    assert capsys.readouterr().out == "File not found\n"
    assert uses_try(assignment.TotalOfFile), "TotalOfFile() must use try / except."
