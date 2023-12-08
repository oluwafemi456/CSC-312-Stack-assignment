#question 4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors_stack(num):
    stack = []
    factor = 2

    while factor <= num:
        if num % factor == 0 and is_prime(factor):
            stack.append(factor)
            num //= factor
        else:
            factor += 1

    while stack:
        print(stack.pop(), end=' ')

# Get input from the user
try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Please enter a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Prime factors of {num} in descending order:")
    prime_factors_stack(num)


#question 5

def binary_to_decimal(binary):
    stack = []
    decimal = 0
    weight = 0

    for bit in binary[::-1]:  # Process bits from right to left
        if bit == '1':
            decimal += 2 ** weight
        weight += 1

    return decimal

def test_binary_to_decimal():
    test_values = ["11000101", "10101010", "11111111", "10000000", "1111100000"]

    for binary in test_values:
        decimal = binary_to_decimal(binary)
        print(f"Binary: {binary} -> Decimal: {decimal}")

# Test the function
test_binary_to_decimal()


#question 6

def decimal_to_binary(decimal):
    stack = []

    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2

    binary = ''.join(stack[::-1])
    return binary if binary else "0"

def test_decimal_to_binary():
    test_values = [197, 170, 255, 128, 992]

    for decimal in test_values:
        binary = decimal_to_binary(decimal)
        print(f"Decimal: {decimal} -> Binary: {binary}")

# Test the function
test_decimal_to_binary()


#question 7

def infix_to_postfix(infix_expr):
    def precedence(operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def is_operator(char):
        return char in {'+', '-', '*', '/', '^'}

    postfix = []
    stack = []

    for token in infix_expr:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Discard the '('
        elif is_operator(token):
            while stack and precedence(stack[-1]) >= precedence(token):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)

# Test the function
infix_expression = "3 + 5 * ( 2 - 8 ) / 2"
postfix_expression = infix_to_postfix(infix_expression.split())
print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {postfix_expression}")
