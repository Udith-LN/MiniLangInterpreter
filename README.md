# **MiniLangInterpreter**

A lightweight interpreter for a custom mini-language, supporting basic arithmetic, variable assignments, and print statements. The interpreter includes features like nested parentheses, operator precedence, and robust error handling.

---

## **Features**
- Arithmetic operations: `+`, `-`, `*`, `/`, `%`
- Variable assignments
- Print statements
- Nested parentheses
- Operator precedence
- Comprehensive error handling:
  - Undefined variables
  - Division/Modulus by zero
  - Invalid characters
  - Incomplete expressions

---

## **Getting Started**

### **Prerequisites**
- Python 3.7 or later

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Udith-LN/MiniLangInterpreter.git
   cd MiniLangInterpreter
---

## **Usage**

### **Run the Interpreter**
To execute a MiniLang script, run the `main.py` file:

```bash
python main.py
```
### **Example Code**
Here's an example MiniLang script:

```bash
x = 10;
y = (x + 5) * 2;
print(y);
```

Ecpected Output:
```bash
30
```
## **Project Structure**
```plaintext
MiniLangInterpreter/
│
├── interpreter/               # Core interpreter components
│   ├── __init__.py            # Package initializer
│   ├── tokenizer.py           # Tokenizer module
│   ├── parser.py              # Parser module
│   ├── ast_nodes.py           # Abstract Syntax Tree (AST) node definitions
│   ├── interpreter.py         # Interpreter module
│
├── tests/                     # Test cases
│   ├── __init__.py            # Test package initializer
│   ├── test_interpreter.py    # Unit tests for the interpreter
│
├── main.py                    # Entry point for the interpreter
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
```
## **Contributions**
Contributions are welcome! Please fork the repository and submit a pull request.
