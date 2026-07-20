import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello, world", "Hello, world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  hello", "hello")
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", True),
    ("skypro", "x", False),
    ])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "k", "Sypro"),
    ("Hello", "l", "Heo"),
    ])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", " "),
    (None, " ")
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize("") == ""


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ])
def test_trim_negative_invalid_types(invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("1kypro", "s", False),
    ("None", "x", False),
    ])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    (None, "y", False),
    ])
def test_contains_negative_invalid_types(invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "n", "Skypro"),
    ("Hello", "b", "Hello"),
    ])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    None,
    ])
def test_delete_simbol_negative_invalid_types(invalid_input):
    with pytest.raises(AttributeError):
        string_utils.trim(invalid_input)
