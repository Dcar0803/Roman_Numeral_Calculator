import sys
import re
from roman_numerals import roman_to_integer, integer_to_roman

class Node:
    """Node class for representing the components of an expression."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.operator = None

class RomanNumeralCalculator:
    @staticmethod
    def main():
        """The main function to run the Roman numeral calculator."""
        if len(sys.argv) < 2:
            print("The calculator requires an expression to calculate.")
            return

        expression = ' '.join(sys.argv[1:])

        # Check if the expression is just a single Roman numeral without operations
        if re.fullmatch(r'[IVXLCDM]+', expression.strip()):
            try:
                # Convert Roman numeral to integer and print it
                result = roman_to_integer(expression.strip())
                print(result)
                return
            except ValueError:
                print("I don't know how to read this.")
                return

        
        result = RomanNumeralCalculator.eval_expression(expression)
        print(result)

    @staticmethod
    def eval_expression(expression):
        """Evaluate the Roman numeral expression."""
        expression = re.sub(r'\s+', '', expression)

        # Replace Roman numerals with the integer
        try:
            expression = re.sub(r'[IVXLCDM]+', lambda x: str(roman_to_integer(x.group())), expression)
        except ValueError:
            return "I don't know how to read this."

        # Parse and evaluate the expression with operator precedence
        try:
            result = RomanNumeralCalculator._evaluate_tree(expression)
        except ZeroDivisionError:
            return "There is no concept of a fractional number in Roman numerals."
        except Exception:
            return "I don't know how to read this."

        if result <= 0:
            return "Negative numbers can't be represented in Roman numerals." if result < 0 else "0 does not exist in Roman numerals."
        elif result > 3999:
            return "You're going to need a bigger calculator."

        return integer_to_roman(result)

    @staticmethod
    def _evaluate_tree(expression):
        """Convert the expression into a tree and evaluate it."""
        # Handle parentheses and brackets
        expression = RomanNumeralCalculator._replace_grouping(expression)

        # Build and evaluate expression tree
        root = RomanNumeralCalculator._build_tree(expression)
        return RomanNumeralCalculator._evaluate_node(root)

    @staticmethod
    def _replace_grouping(expression):
        """Replace brackets with parentheses for consistent parsing."""
        expression = expression.replace('[', '(').replace(']', ')')
        return expression

    @staticmethod
    def _build_tree(expression):
        """Build a tree for the expression with correct operator precedence."""
        # Use a stack-based approach to build an expression tree with precedence
        # Define operators precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        
        tokens = re.findall(r'\d+|[()+*/-]', expression)
        stack = []
        output = []
        
        for token in tokens:
            if token.isdigit():
                output.append(Node(int(token)))
            elif token in precedence:
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                    output.append(Node(stack.pop()))
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(Node(stack.pop()))
                stack.pop()

        while stack:
            output.append(Node(stack.pop()))

        return RomanNumeralCalculator._construct_tree(output)

    @staticmethod
    def _construct_tree(postfix):
        """Constructs an expression tree from postfix notation."""
        stack = []
        for token in postfix:
            if isinstance(token.value, int):
                stack.append(token)
            else:
                node = token
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack[0]

    @staticmethod
    def _evaluate_node(node):
        """Evaluate the tree from the given node."""
        if isinstance(node.value, int):
            return node.value
        
        left_value = RomanNumeralCalculator._evaluate_node(node.left)
        right_value = RomanNumeralCalculator._evaluate_node(node.right)

        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            if right_value == 0:
                raise ZeroDivisionError
            return left_value // right_value

# Run the program when called from the command line
if __name__ == "__main__":
    RomanNumeralCalculator.main()
