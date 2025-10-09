import pytest
from string_utils import StringUtils


@pytest.mark.positive_test
@pytest.mark.parametrize('num1, result', [("apple", "Apple"),
                                          ("PEAR", "Pear"),
                                          ("апельсин", "Апельсин")])
def test_positive_capitalize(num1, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(num1)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('num1, result', [("123abc", "123abc"),
                                          ("", ""),
                                          ("!@#r", "!@#r")])
def test_negative_capitalize(num1, result):
    stringutils = StringUtils()
    res = stringutils.capitalize(num1)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('num1, result', [("   apple", "apple"),
                                          ("   PEAR", "PEAR"),
                                          ("   апельсин", "апельсин")])
def test_positive_trim(num1, result):
    stringutils = StringUtils()
    res = stringutils.trim(num1)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('num1, result', [("   !@#r", "!@#r"),
                                          ("    ", ""),
                                          ("   123abc", "123abc")])
def test_negative_trim(num1, result):
    stringutils = StringUtils()
    res = stringutils.trim(num1)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('num1, num2, result', [("Apple", "A", True),
                                                ("Pear", "A", False),
                                                ("Апельсин", "н", True)])
def test_positive_contains(num1, num2, result):
    stringutils = StringUtils()
    res = stringutils.contains(num1, num2)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('num1, num2, result', [("Apple", "4", False),
                                                (" ", " ", True),
                                                ("=-09", "9", True)])
def test_negative_contains(num1, num2, result):
    stringutils = StringUtils()
    res = stringutils.contains(num1, num2)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('num1, num2, result', [("tApple", "t", "Apple"),
                                                ("PeRar", "R", "Pear"),
                                            ("Orange123", "123", "Orange")])
def test_positive_delete_symbol(num1, num2, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(num1, num2)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('num1, num2, result', [("   ", "   ", ""),
                                                ("Pear", "Pear", ""),
                                                ("Orange", None, "Orange")])
def test_negative_delete_symbol(num1, num2, result):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(num1, num2)
    assert res == result
