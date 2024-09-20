import pytest
from main import RomanNumeralCalculator

def test_basic_addition():
    assert RomanNumeralCalculator.eval_expression("X + V") == "XV"

def test_basic_subtraction():
    assert RomanNumeralCalculator.eval_expression("X - V") == "V"

def test_multiplication():
    assert RomanNumeralCalculator.eval_expression("X * II") == "XX"

def test_division():
    assert RomanNumeralCalculator.eval_expression("X / II") == "V"

def test_grouping():
    assert RomanNumeralCalculator.eval_expression("(X + V) * II") == "XXX"

def test_invalid_expression():
    assert RomanNumeralCalculator.eval_expression("X + [V") == "I don't know how to read this."

# Advanced test cases with both parentheses () and brackets []
def test_mixed_grouping_simple():
    """Test case with both parentheses and brackets."""
    assert RomanNumeralCalculator.eval_expression("(X + V) * [II + I]") == "XLV"  # (10 + 5) * (2 + 1) = 15 * 3 = 45

def test_nested_grouping():
    """Test case with nested parentheses and brackets."""
    assert RomanNumeralCalculator.eval_expression("((X + V) * (II + I)) / [III]") == "XV"  # (15 * 3) / 3 = 15

def test_complex_grouping():
    """Test case with complex grouping and multiple operators."""
    assert RomanNumeralCalculator.eval_expression("[(X + II) * (V + I)] / (III)") == "XXIV"  # ((12 * 6) / 3) = 24

def test_mixed_operations_and_grouping():
    """Test case with a mix of operations, including division and subtraction."""
    assert RomanNumeralCalculator.eval_expression("((X * II) - (V + III)) + [X]") == "XVII"  # ((10 * 2) - (5 + 3)) + 10 = 17

def test_nested_brackets_and_parentheses():
    """Test with multiple nested levels of brackets and parentheses."""
    assert RomanNumeralCalculator.eval_expression("[((X + V) * II) + (V / I)]") == "XXXV"  # ((10 + 5) * 2) + (5 / 1) = 35

# Edge cases with invalid or complex scenarios
def test_invalid_brackets():
    """Test case with invalid or mismatched brackets."""
    assert RomanNumeralCalculator.eval_expression("[X + V") == "I don't know how to read this."

def test_invalid_characters():
    """Test case with invalid characters."""
    assert RomanNumeralCalculator.eval_expression("X + & V") == "I don't know how to read this."

def test_large_numbers():
    """Test case where the result exceeds the maximum allowed Roman numeral (3999)."""
    assert RomanNumeralCalculator.eval_expression("(M * IV) + (D * III)") == "You're going to need a bigger calculator."

def test_zero_result():
    """Test case that would result in zero, which is not valid in Roman numerals."""
    assert RomanNumeralCalculator.eval_expression("X - X") == "0 does not exist in Roman numerals."

def test_negative_result():
    """Test case that results in a negative number, which is not valid in Roman numerals."""
    assert RomanNumeralCalculator.eval_expression("V - X") == "Negative numbers can't be represented in Roman numerals."

def test_fractional_result():
    """Test case that would result in a fraction, which is not valid in Roman numerals."""
    assert RomanNumeralCalculator.eval_expression("V / II") == "II"  # Roman numerals use integer division

def test_division_by_zero():
    """Test case with division by zero, which should raise an error."""
    assert RomanNumeralCalculator.eval_expression("X / 0") == "There is no concept of a fractional number in Roman numerals."