from collections import deque

class Validator:

    def brackets_check(expression: str) -> bool:

        brackets: deque = deque()

        try:

            for symbol in expression:

                match symbol:
                    case "(": brackets.append(symbol)
                    case ")": brackets.pop()

        except IndexError: return False
                    
        return not brackets

    def syntax_check(expression: str) -> bool:

        expr_len = len(expression)
        is_correct: bool = 1
        variables = "abcde"

        if expr_len == 1 and expression[0] in variables:
            return is_correct

        for i, symbol in enumerate(expression):

            if not is_correct: break

            match symbol:
                          
                case "→"|"&"|"|"|"~":
                    
                    if not i or i == expr_len - 1: 
                        is_correct = 0
                        break    

                    is_correct = bool(expression[i - 1] in (variables + ")") and
                                      expression[i + 1] in (variables + "!("))
                    
                    continue
                    
                case "a"|"b"|"c"|"d"|"e":

                    if not i:
                        is_correct = bool(expression[i + 1] in "→&|~)")
                        continue
                    elif i == expr_len - 1:
                        is_correct = bool(expression[i - 1] in "(→&|~!")
                        continue

                    is_correct = bool(expression[i - 1] not in variables and
                                      expression[i + 1] not in variables)
                    
                    continue

                case "!": 

                    if i == expr_len - 1:
                        is_correct = 0
                        break
                    elif not i:
                        is_correct = bool(expression[i + 1] in variables)
                        continue

                    is_correct = bool(expression[i + 1] in variables and 
                                      expression[i - 1] not in variables)
                    
                    continue

                case "(": 

                    if i == expr_len - 1:
                        is_correct = 0
                        break
                    
                    is_correct = bool(expression[i + 1] in (variables + "(!"))
                    continue

                case ")": 

                    if not i:
                        is_correct = 0
                        break
                    
                    is_correct = bool(expression[i - 1] in (variables + ')'))
                    continue

                case _: is_correct = 0

        return is_correct

    def is_valid(expression: str) -> bool: 
        return (Validator.syntax_check(expression) and 
                Validator.brackets_check(expression))




