'''Computes RPN expressions'''

import argparse

def calculate(num1, num2, operator):
    '''Perform computation for the numbers
       :param num1: first number
       :param num2: second number
       :param operator: valid math operator
       :return int: result'''

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num2 - num1
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num2 / num1
    else:
        raise TypeError("Invalid Operator")

def process(equation):
    '''Arrange the equation using stack
       :param equation: valid RPN equation in string format
       :return result'''

    stack = []
    for token in equation:
        if not token.isspace():
            if token.isdigit():
                stack.append(token)
            else:
                if len(stack) < 2: raise TypeError("Invalid Equation")
                num1 = stack.pop()
                num2 = stack.pop()
                result = calculate(int(num1), int(num2), token)
                stack.append(result)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process RPN equation')
    parser.add_argument(
        '--input',
        required=True,
        help='Input Equation')
    known_args, pipeline_args = parser.parse_known_args()
    equation = vars(known_args)['input']
    result = process(equation)
    print(result)
