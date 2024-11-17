import pytest
from stringutils import StringUtils


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("HELLO world", "Hello world"),
    ],
)
def test_capitilize_positive(input, expected_output):
    res = StringUtils()
    assert res.capitilize(input) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("85/", "85/"),
        ("   ", "   "),
    ],
)
def test_capitilize_negative(input, expected_output):
    res = StringUtils()
    assert res.capitilize(input) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("   Hello", "Hello"),
        ("Hello", "Hello"),
        ("   562", "562"),
        ("   ", "")
    ],
)
def test_trim_positive(input, expected_output):
    res = StringUtils()
    assert res.trim(input) == expected_output


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("Hello   ", "Hello"),
        ("562   ", "562"),
        ("   ", "")
    ],
)
def test_trim_negative(input, expected_output):
    res = StringUtils()
    assert res.trim(input) == expected_output


@pytest.mark.parametrize(
    "input, delimeter, result",
    [("Cat,Dog,Frog", ",", ["Cat", "Dog", "Frog"])],
)
def test_to_list_positive(input, delimeter, result):
    res = StringUtils()
    assert res.to_list(input, delimeter) == result


@pytest.mark.parametrize(
    "input, delimeter, result",
    [("", ",", []),
     ("   ", ",", [])],
)
def test_to_list_negative(input, delimeter, result):
    res = StringUtils()
    assert res.to_list(input, delimeter) == result


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "C"),
        ("Dog", "D")
    ],
)
def test_contains_positive(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == (True)


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "F"),
        ("Dog", "H")
    ],
)
def test_contains_negative(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == (False)


@pytest.mark.parametrize(
    "input, symbol, expected_output",
    [
        ("Cat", "a", "Ct"),
        ("Hello", "He", "llo"),
        ("Hello", "", "Hello"),
    ],
)
def test_delete_symbol_positive(input, symbol, expected_output):
    res = StringUtils()
    assert res.delete_symbol(input, symbol) == expected_output


@pytest.mark.xfail
@pytest.mark.parametrize(
    "input, symbol, expected_output",
    [
        ("Dog", "a", "Dg"),
        ("Hello", "R", "ello"),
    ],
)
def test_delete_symbol_negative(input, symbol, expected_output):
    res = StringUtils()
    assert res.delete_symbol(input, symbol) == expected_output


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "C"),
        ("Dog", "D")
    ],
)
def test_starts_with_positive(input, symbol):
    res = StringUtils()
    assert res.starts_with(input, symbol) == (True)


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "F"),
        ("Dog", "H")
    ],
)
def test_starts_with_negative(input, symbol):
    res = StringUtils()
    assert res.starts_with(input, symbol) == (False)


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "t"),
        ("Dog", "g")
    ],
)
def test_end_with_positive(input, symbol):
    res = StringUtils()
    assert res.end_with(input, symbol) == (True)


@pytest.mark.parametrize(
    "input, symbol",
    [
        ("Cat", "a"),
        ("Dog", "o")
    ],
)
def test_starts_end_with(input, symbol):
    res = StringUtils()
    assert res.end_with(input, symbol) == (False)


@pytest.mark.parametrize(
    "input",
    [
        (""),
        ("  ")
    ],
)
def test_is_empty_positive(input):
    res = StringUtils()
    assert res.is_empty(input) == (True)


@pytest.mark.parametrize(
    "input",
    [
        ("Cat"),
        ("563")
    ],
)
def test_is_empty_with(input):
    res = StringUtils()
    assert res.is_empty(input) == (False)


@pytest.mark.parametrize(
    "list, joiner, expected_output",
    [
        ([1, 2, 3, 4], ',', '1,2,3,4'),
        (["moon", "river"], '-', "moon-river"),
        (["free", "service"], ':', "free:service"),
    ],
)
def test_list_to_string_positive(list, joiner, expected_output):
    res = StringUtils()
    assert res.list_to_string(list, joiner) == expected_output


@pytest.mark.parametrize(
    "list, joiner, expected_output",
    [
        (["   ", "   "], '-', "   -   "),
        (["free", "service"], ' ', "free service"),
    ],
)
def test_list_to_string_negative(list, joiner, expected_output):
    res = StringUtils()
    assert res.list_to_string(list, joiner) == expected_output
