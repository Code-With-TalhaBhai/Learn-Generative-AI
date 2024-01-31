# Note: If you are not writing test_cases inside `tests` folder, then you can run this file by `pytest [file_name]` 
# And, If you are writing test_cases inside `tests` folder, then only type `pytest` all test_cases run automatically


# To avoid addition information use `-q` as `pytest -q [file_name.py]`

def func(x:int)->int:
    return x + 1

def func1(x:int)->int:
    return x + 1


# test cases
# If you want to write testcases, it is important to write prefix of `test`,
# before function name, as test_answer()
def test_answer1():
    assert func(5) == 65


def test_answer2():
    assert func1(45) == 46

