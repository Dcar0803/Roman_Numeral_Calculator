# Roman Numerals to Integers
roman_numerals_to_integers = {
    "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
    "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
}

# Integers to Roman Numerals
integers_to_roman_numerals = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
    (5, 'V'), (4, 'IV'), (1, 'I')
]

def roman_to_integer(roman):
    '''Converts a Roman numeral to an integer'''
    result = 0
    # Loop through each character in the Roman numeral string
    for character in range(len(roman)):
        # If the current numeral is larger than the previous one, apply the subtraction rule
        if character > 0 and roman_numerals_to_integers[roman[character]] > roman_numerals_to_integers[roman[character - 1]]:
            result += roman_numerals_to_integers[roman[character]] - 2 * roman_numerals_to_integers[roman[character - 1]]
        else:
            result += roman_numerals_to_integers[roman[character]]
    return result

def integer_to_roman(number):
    '''Converts an integer to a Roman numeral'''
    if number <= 0:
        raise ValueError("Roman numerals cannot represent zero or negative numbers.")
    if number > 3999:
        raise ValueError("Roman numerals cannot represent numbers greater than 3999.")

    result = []
    for value, numeral in integers_to_roman_numerals:
        # While the number is greater than the current value, subtract the value and add the numeral to the result
        while number >= value:
            result.append(numeral)
            number -= value
    return ''.join(result)

# Testing the functions
if __name__ == "__main__":
    print(roman_to_integer("XIV"))  # Output: 14
    print(roman_to_integer("MCMXCIV"))  # Output: 1994
    print(roman_to_integer("MMXXIV"))  # Output: 2024

    print(integer_to_roman(14))  # Output: XIV
    print(integer_to_roman(1994))  # Output: MCMXCIV
    print(integer_to_roman(2024))  # Output: MMXXIV
