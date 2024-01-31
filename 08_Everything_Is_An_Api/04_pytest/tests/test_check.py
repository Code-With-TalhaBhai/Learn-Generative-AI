
# If you are writing test inside tests folder then test filename should hav prefix of `test` as this is test_check.py

def func(x:int)->int:
    return x + 1

def func1(x:int)->int:
    return x + 1


# test cases
# If you want to write testcases, it is important to write prefix of `test`,
# before function name, as test_answer()
def test_check1():
    assert func(5) == 65


def test_check2():
    assert func1(45) == 46


# Note: write pytest in terminal to run this file and execute test cases