from solution import appearance
from solution import tests


def test_appearance():
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert test_answer == test["answer"], (
            f"Error on test case {i}, got {test_answer}, expected {test['answer']}"
        )


def test_check_intervals():
    for i, test in enumerate(tests):
        test = test["intervals"]
        for j in test:
            assert len(test[j]) % 2 == 0
            if len(test[j]) % 2 != 0:
                raise ValueError("Некорректное количество интервалов")
