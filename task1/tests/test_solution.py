import pytest

from solution import sum_two


class TestSumTwo:
    @pytest.mark.parametrize(
        "a, b, res, raises",
        [
            (2, 4, 6, None),
            (2, 4.5, None, TypeError),
            (2, True, None, TypeError),
            (2, False, None, TypeError),
            (2, "", None, TypeError),
        ],
    )
    def test_solution_false(self, a, b, res, raises):
        if raises:
            with pytest.raises(raises):
                sum_two(a, b)
        else:
            assert sum_two(a, b) == res
