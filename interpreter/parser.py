class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            raise SyntaxError(f"Expected {expected_type}, but found {token[1]} at position {self.pos}")
        else:
            raise SyntaxError(f"Unexpected end of input; expected {expected_type}")

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][0] == 'IDENTIFIER':
                statements.append(self.parse_assignment())
            elif self.tokens[self.pos][0] == 'PRINT':
                statements.append(self.parse_print())
            else:
                token = self.tokens[self.pos]
                raise SyntaxError(f"Unexpected token: {token[1]} at position {self.pos}")
        return statements

    def parse_assignment(self):
        var_name = self.consume('IDENTIFIER')[1]
        self.consume('ASSIGN')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return AssignNode(var_name, value)

    def parse_print(self):
        self.consume('PRINT')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return PrintNode(value)

    def parse_expression(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Incomplete expression: unexpected end of input")
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('PLUS', 'MINUS'):
            op = self.consume(self.tokens[self.pos][0])[0]
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] not in ('NUMBER', 'IDENTIFIER', 'LPAREN'):
                raise SyntaxError(f"Expected a term after operator {op}, but found {self.tokens[self.pos][1]} at position {self.pos}")
            right = self.parse_term()
            left = BinOpNode(left, op, right)
        return left
            
    def parse_term(self):
        left = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('MULTIPLY', 'DIVIDE', 'MODULUS'):
            op = self.consume(self.tokens[self.pos][0])[0]
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] not in ('NUMBER', 'IDENTIFIER', 'LPAREN'):
                raise SyntaxError(f"Expected a term after operator {op}, but found {self.tokens[self.pos][1]} at position {self.pos}")
            right = self.parse_factor()
            left = BinOpNode(left, op, right)
        return left

    def parse_factor(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Incomplete expression: expected a factor but found end of input")
        token = self.tokens[self.pos]
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return NumberNode(int(token[1]))
        elif token[0] == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            return VariableNode(token[1])
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()  # Parse the inner expression
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != 'RPAREN':
                raise SyntaxError(f"Missing closing parenthesis for expression starting at position {self.pos - 1}")
            self.consume('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Invalid factor: {token[1]} at position {self.pos}")
