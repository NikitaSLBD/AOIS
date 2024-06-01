from validator import Validator

class ValidateError(Exception):
    pass

def parse_brackets(open_bracket_index: int, expression: str) -> str:

    brackets: int = 1
    expression = expression[open_bracket_index + 1:]
    result = ""

    for symbol in str(expression):

        if symbol == '(': brackets += 1
        elif symbol == ')': brackets -= 1

        if not brackets: break

        result += symbol

    return result

class LogicalOperation():

    def __init__(self, operation: chr, right_op=None, left_op=None):

        self.__operation = operation
        self.__right_operand = right_op
        self.__left_operand = left_op

    def get_operation(self): return self.__operation
    def get_right_operand(self): return self.__right_operand
    def get_left_operand(self): return self.__left_operand

    def __str__(self):

        left_op = str(self.get_left_operand())
        operation = str(self.get_operation())
        right_op = str(self.get_right_operand())

        if left_op == "None": left_op = ''
        elif isinstance(left_op, LogicalOperation):
            left_op = str(left_op)
        if isinstance(right_op, LogicalOperation):
            right_op = str(right_op)

        return f"{left_op}{operation}{right_op}"


def parse_expression(expression: str) -> LogicalOperation:

    i = 0
    while i < len(expression):
        match expression[i]:
            case 'a'|'b'|'c'|'d'|'e':
                logical_operations = expression[i]
                i += 1
            
            case '!': 
                if expression[i + 1] != '(':
                    logical_operations = LogicalOperation('!', expression[i + 1])
                    i += 2
                    continue
                
                bracket_expression = parse_brackets(i + 1, expression)
                logical_operations = LogicalOperation('!', parse_expression(bracket_expression))
                i += len(bracket_expression) + 3
                continue 
                
            case '|'|'&'|'→'|'~':
                if expression[i + 1] == '(': 
                    bracket_expression = parse_brackets(i + 1, expression)
                    logical_operations = LogicalOperation(expression[i], parse_expression(bracket_expression),
                                                          logical_operations)
                    i += len(bracket_expression) + 3
                    continue

                elif expression[i + 1] == '!' and expression[i + 2] != '(':
                    logical_operations = LogicalOperation(expression[i], parse_expression(expression[i + 1:i + 3]),
                                                          logical_operations)
                    i += 3
                    continue
                
                elif expression[i + 1] == '!' and expression[i + 2] == '(':
                    bracket_expression = parse_brackets(i + 2, expression)
                    logical_operations = LogicalOperation(expression[i], parse_expression(f"!({bracket_expression})"),
                                                          logical_operations)
                    i += len(bracket_expression) + 3
                    continue

                logical_operations = LogicalOperation(expression[i], expression[i + 1], logical_operations)
                i += 2

            case '(': 
                if not i:
                    bracket_expression = parse_brackets(i, expression)
                    logical_operations = parse_expression(bracket_expression)
                    i += len(bracket_expression) + 2
    
    return logical_operations

class LogicalExpression:

    def __init__(self, expression: str):

        logical_expression = expression.replace("->", '→')

        if Validator.is_valid(logical_expression):
            self.__expression = logical_expression
        else: raise ValidateError("")

        self.__variables = sorted(list(set(filter(lambda a: a.isalpha(), logical_expression))))
        self.__logical_operations = parse_expression(logical_expression)


    def __str__(self): return self.__expression

    def get_logical_operations(self): return self.__logical_operations
    def get_variables(self): return self.__variables

    