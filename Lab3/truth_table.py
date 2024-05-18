from logical_expression import LogicalExpression, LogicalOperation 

def adding(bin1: str, bin2: str) -> str:
    result = ""
    carry = False

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    for i in range(max_len - 1, 0, -1):

        if (bin1[i] == "1" and bin2[i] == "1"):
            
            if carry:
                result = "1" + result
            else:
                result = "0" + result
                carry = True
                continue

        elif (bin1[i] == "0" and bin2[i] == "0"):

            if carry:
                result = "1" + result
                carry = False
            else: result = "0" + result 

        else:

            if carry:
                result = "0" + result
            else: result = "1" + result 

    result = result.zfill(31)

    return result

def values_generator(var_count: int):

    values = "0" * var_count

    while values != "1" * var_count:

        yield list(map(lambda bit: int(bool(int(bit))), values))
        values = adding('0' + values, "1".zfill(var_count + 1))[-var_count:]
    
    else: yield list(map(lambda bit: int(bool(int(bit))), values))

def solve_tree(logical_tree: LogicalOperation, variables: dict, operations: dict={}): 

    if isinstance(logical_tree, str):
        return variables[logical_tree], operations

    if not logical_tree.get_left_operand():
        str_op = str(logical_tree)
        operations[str_op] = int(not solve_tree(logical_tree.get_right_operand(), variables, operations)[0])
        return operations[str_op], operations

    left_value = solve_tree(logical_tree.get_left_operand(), variables, operations)[0]
    right_value = solve_tree(logical_tree.get_right_operand(), variables, operations)[0]
    str_op = str(logical_tree)

    match logical_tree.get_operation():
        case '&': 
            operations[str_op] = int(left_value and right_value)
            return operations[str_op], operations
        case '|': 
            operations[str_op] = int(left_value or right_value)
            return operations[str_op], operations
        case '→': 
            operations[str_op] = int(not left_value or right_value)
            return operations[str_op], operations
        case '~': 
            operations[str_op] = int(left_value == right_value)
            return operations[str_op], operations
        
    return operations

def get_truth_table(logical_expr: LogicalExpression):

    logic_vars = logical_expr.get_variables()
    truth_table = []

    list_values = values_generator(len(logic_vars))

    for values in list_values:

        variables = dict(zip(logic_vars, values))
        yield variables, solve_tree(logical_expr.get_logical_operations(), variables)[1]
        
        
        

    