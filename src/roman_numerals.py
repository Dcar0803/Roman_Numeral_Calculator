import re

roman_numerals_to_integers = {
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
    "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
}

integers_to_roman_numerals = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
    (5, 'V'), (4, 'IV'), (1, 'I')
]

def is_valid_roman(numeral):
    """
    Check if a Roman numeral string is valid according to Roman numeral rules.

    Args:
        numeral (str): Roman numeral string to validate.

    Returns:
        bool: True if the numeral is valid, False otherwise.
    """
    valid_roman_pattern = (
        r"^M{0,3}"  # Thousands - 0 to 3 M's
        r"(CM|CD|D?C{0,3})"  
        r"(XC|XL|L?X{0,3})"  
        r"(IX|IV|V?I{0,3})$"  
    )
    return re.match(valid_roman_pattern, numeral) is not None

def roman_to_integer(roman):
    """
    Convert a Roman numeral string to an integer after validating its correctness.

    Args:
        roman (str): Roman numeral string.

    Returns:
        int: The integer representation of the Roman numeral.

    Raises:
        ValueError: If the Roman numeral is invalid.
    """
    if not is_valid_roman(roman):
        raise ValueError(f"Invalid Roman numeral: {roman}")

    result = 0
    for i in range(len(roman)):
        if i > 0 and roman_numerals_to_integers[roman[i]] > roman_numerals_to_integers[roman[i - 1]]:
            result += roman_numerals_to_integers[roman[i]] - 2 * roman_numerals_to_integers[roman[i - 1]]
        else:
            result += roman_numerals_to_integers[roman[i]]
    return result

def integer_to_roman(number):
    """
    Convert an integer to a Roman numeral string.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the integer.

    Raises:
        ValueError: If the number is <= 0 or > 3999.
    """
    if number <= 0:
        raise ValueError("Roman numerals cannot represent zero or negative numbers.")
    if number > 3999:
        raise ValueError("Roman numerals cannot represent numbers greater than 3999.")

    result = []
    for value, numeral in integers_to_roman_numerals:
        while number >= value:
            result.append(numeral)
            number -= value
    return ''.join(result)
