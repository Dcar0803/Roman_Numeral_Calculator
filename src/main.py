import sys  # For handling command-line input
import re   # For working with regular expressions
from roman_numerals import roman_to_integer, integer_to_roman  

class Roman_Numeral_Calculator:

    @staticmethod
    def main():
        """The main function to run the Roman numeral calculator."""
        if len(sys.argv) < 2:
            print("The calculator requires an expression to calculate.")
            return

        # Combines the entire command-line input into a single string
        expression = ' '.join(sys.argv[1:])
        result = Roman_Numeral_Calculator.eval_expression(expression)
        print(result)

    @staticmethod
    def eval_expression(expression):
        """This function evaluates the Roman numeral equation."""
        # Remove any whitespace
        expression = re.sub(r'\s+', '', expression)

        # Replace Roman numerals with their integer equivalents
        try:
            expression = re.sub(r'[IVXLCDM]+', lambda x: str(roman_to_integer(x.group())), expression)
        except ValueError:
            return "I don't know how to read this."

        try:
            # Evaluate the expression using Python's eval function
            result = eval(expression)
        except ZeroDivisionError:
            return "There is no concept of a fractional number in Roman numerals."
        except Exception:
            return "I don't know how to read this."

        # Handle the result based on Roman numeral constraints
        if result <= 0:
            return "Negative numbers can’t be represented in Roman numerals." if result < 0 else "0 does not exist in Roman numerals."
        elif result > 3999:
            return "You’re going to need a bigger calculator."

        # Convert the result back to Roman numerals and return it
        return integer_to_roman(result)

# Run the program when called from the command line
if __name__ == "__main__":
    Roman_Numeral_Calculator.main()
