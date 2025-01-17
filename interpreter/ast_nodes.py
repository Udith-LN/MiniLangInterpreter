class ASTNode:
    pass

class AssignNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name
