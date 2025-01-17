from interpreter import Interpreter
from parser import Parser
from tokenizer import tokenize

if __name__ == "__main__":
    code = """
    x = 10;
    y = (x + 5) * 2;
    print(y);
    """
    tokens = tokenize(code)
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast)
