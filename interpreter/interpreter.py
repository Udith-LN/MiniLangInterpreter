class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, nodes):
        for node in nodes:
            if isinstance(node, AssignNode):
                value = self.evaluate(node.value)
                self.variables[node.name] = value
            elif isinstance(node, PrintNode):
                result = self.evaluate(node.value)
                print(result)

    def evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, VariableNode):
            value = self.variables.get(node.name)
            if value is None:
                raise NameError(f"Undefined variable: {node.name}")
            return value
        elif isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == 'PLUS':
                return left + right
            elif node.op == 'MINUS':
                return left - right
            elif node.op == 'MULTIPLY':
                return left * right
            elif node.op == 'DIVIDE':
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                return left / right
            elif node.op == 'MODULUS':
                if right == 0:
                    raise ZeroDivisionError("Modulus by zero is not allowed")
                return left % right
            else:
                raise ValueError(f"Unsupported operator: {node.op}")
        else:
            raise ValueError(f"Unknown node type: {node}")