import re

# Define token types
TOKEN_SPEC = [
    ('PRINT', r'print'),          # Print keyword
    ('NUMBER', r'\d+'),           # Integer
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Variable names
    ('ASSIGN', r'='),             # Assignment operator
    ('PLUS', r'\+'),              # Addition
    ('MINUS', r'-'),              # Subtraction
    ('MULTIPLY', r'\*'),          # Multiplication
    ('DIVIDE', r'/'),             # Division
    ('MODULUS', r'%'),            # Modulus
    ('LPAREN', r'\('),            # Left parenthesis
    ('RPAREN', r'\)'),            # Right parenthesis
    ('SEMICOLON', r';'),          # End of statement
    ('SKIP', r'[ \t]+'),          # Skip spaces and tabs
    ('MISMATCH', r'.')            # Any other character
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    position = 0
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            position += len(value)  # Skip whitespace but track position
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character: {value} at position {position}")
        tokens.append((kind, value))
        position += len(value)
    return tokens
