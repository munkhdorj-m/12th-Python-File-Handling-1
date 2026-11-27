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


def test1_read_numbers(tmp_path):
    path = make_file(tmp_path, "numbers.txt", "12\n7\n-3\n40\n")
    assert assignment.ReadNumbers(path) == [12, 7, -3, 40]
    path = make_file(tmp_path, "one.txt", "5")
    assert assignment.ReadNumbers(path) == [5]


def test1_skips_bad_lines(tmp_path):
    path = make_file(tmp_path, "numbers.txt", "5\nabc\n\n3.5\n8\ntwenty\n-2\n9")
    assert assignment.ReadNumbers(path) == [5, 8, -2, 9]
    path = make_file(tmp_path, "bad.txt", "x\ny\n")
    assert assignment.ReadNumbers(path) == []


def test1_empty_file(tmp_path):
    path = make_file(tmp_path, "empty.txt", "")
    assert assignment.ReadNumbers(path) == []


def test1_file_not_found(tmp_path, capsys):
    assert assignment.ReadNumbers(str(tmp_path / "missing.txt")) == []
    assert "File not found" in capsys.readouterr().out
    assert uses_try(assignment.ReadNumbers), "ReadNumbers() must use try / except."


def test2_write_scores(tmp_path):
    path = str(tmp_path / "scores.txt")
    assert assignment.WriteScores(path, [["Anu", 85], ["Bat", 62], ["Tom", 7]]) == True
    assert read_file(path) == "Anu,85\nBat,62\nTom,7\n"


def test2_overwrites_and_empty(tmp_path):
    path = make_file(tmp_path, "scores.txt", "Old,1\nOld,2\n")
    assert assignment.WriteScores(path, [["Saraa", 90]]) == True
    assert read_file(path) == "Saraa,90\n"
    assert assignment.WriteScores(path, []) == True
    assert read_file(path) == ""


def test2_cannot_write(tmp_path, capsys):
    assert assignment.WriteScores(str(tmp_path), [["Anu", 85]]) == False
    assert "Cannot write to file" in capsys.readouterr().out
    path = str(tmp_path / "no_folder" / "scores.txt")
    assert assignment.WriteScores(path, [["Anu", 85]]) == False
    assert "Cannot write to file" in capsys.readouterr().out
    assert uses_try(assignment.WriteScores), "WriteScores() must use try / except."


def test3_grades(tmp_path):
    source = make_file(tmp_path, "results.txt", "Anu,85\nBat,62\nTom,40\nSaraa,39\nBold,80\nAnu Bat,60\nNomin,100\nZaya,0\n")
    target = str(tmp_path / "grades.txt")
    assert assignment.ProcessResults(source, target) == 0
    assert read_file(target) == "Anu,A\nBat,B\nTom,C\nSaraa,U\nBold,A\nAnu Bat,B\nNomin,A\nZaya,U\n"


def test3_invalid_lines(tmp_path):
    source = make_file(tmp_path, "results.txt", "Anu,85\nBat\nTom,abc\nSaraa,105\nBold,-1\nZaya,50,70\nNomin,60\nDorj,7.5")
    target = str(tmp_path / "grades.txt")
    assert assignment.ProcessResults(source, target) == 6
    assert read_file(target) == "Anu,A\nNomin,B\n"


def test3_file_not_found(tmp_path, capsys):
    target = str(tmp_path / "grades.txt")
    assert assignment.ProcessResults(str(tmp_path / "missing.txt"), target) == -1
    assert "File not found" in capsys.readouterr().out
    assert uses_try(assignment.ProcessResults), "ProcessResults() must use try / except."
