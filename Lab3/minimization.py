from logical_expression import LogicalExpression
from truth_table import get_truth_table
from forms import get_normal_form

def get_variables(full_normal_form: str) -> list[set]:

    variables = set()
    result = []
    i = 0

    while i < len(full_normal_form):
        if full_normal_form[i] == '(': 
            variables.clear()
            i += 1
        elif full_normal_form[i] == ')': 
            result.append(set(variables))
            i += 1
        elif full_normal_form[i] == '!':
            variables.add(full_normal_form[i:i + 2])
            i += 2
        elif full_normal_form[i].isalpha():
            variables.add(full_normal_form[i])
            i += 1
        else: i += 1

    return result

def delete_duplicates(list):

    result = []
    [result.append(a) for a in list if a not in result]
    return result

def is_reciprocal(variables: set) -> bool:

    if len(variables) != 2: return False

    first_var = variables.pop()
    second_var = variables.pop()

    return first_var == '!' + second_var or \
           first_var == second_var.replace('!', '')


def gluing(variables: list[set], is_print: bool=0):

    variables_count = len(variables[0])
    processed_variables = []
    result = []
    flag = 0
    
    if is_print: print(variables)

    for i in range(len(variables)):
        j = i + 1
        while j < len(variables):

            intersection = variables[i].intersection(variables[j])
            difference = variables[i].symmetric_difference(variables[j])

            if len(intersection) == variables_count - 1 and \
               is_reciprocal(difference):
                
                result.append(intersection)

                processed_variables.append(variables[i])
                processed_variables.append(variables[j])

                flag = 1
                j += 1

            else: j += 1

        else:
            if variables[i] not in processed_variables:
                result.append(set(variables[i]))

    result = delete_duplicates(result)

    if flag: return gluing(result, is_print)
    else: return delete_duplicates(result)

def delete_extra(post_variables: list[set]):

    extras = []

    for implicant in post_variables:
        if len(implicant) != 1: continue

        for variables in post_variables:
            if implicant != variables and implicant.issubset(variables):
                extras.append(variables)

    return [el for el in post_variables if el not in extras]


def get_formula_type(logical_formula: str) -> chr:

    closebracket_index = logical_formula.find(')')
    return logical_formula[closebracket_index + 1]

def minimization(logical_formula): 

    implicants = get_variables(logical_formula)
    formula_type = get_formula_type(logical_formula)

    print("Gluing: ")
    post_variables = gluing(implicants, 1)
    post_variables = delete_extra(post_variables)

    print("Delete extra implicants:")
    print(post_variables)
    
    return get_normal_form(post_variables, formula_type)

def build_table(variables: list[set], post_variables: list[set]):

    implicants = []
    table = {}

    for constituent in variables:
        implicants.clear()
        for implicant in post_variables:
            if implicant.issubset(constituent): implicants.append(implicant)

        table[tuple(constituent)] = delete_duplicates(implicants)

    return table

def table_minimization(logical_formula: str):

    implicants = get_variables(logical_formula)
    formula_type = get_formula_type(logical_formula)

    print("Gluing: ")
    post_variables = gluing(implicants, 1)
    table = build_table(implicants, post_variables)

    print("Implicants table:")
    for key in table:
        print(f"{key}: {table[key]}")

    minimum_variables = []

    for key in table:
        for implicant in post_variables:
            if implicant in table[key] and len(table[key]) == 1:
                minimum_variables.append(implicant)

    minimum_variables = delete_duplicates(minimum_variables)

    print("Delete extra implicant:")
    print(minimum_variables)

    return get_normal_form(minimum_variables, formula_type)

if __name__ == "__main__":

    logical_formula = input("Enter sknf or sdnf: ")

    print("\nCalculation method:")
    print(minimization(logical_formula))
    print("\nTable-calculation method:")
    print(table_minimization(logical_formula))
    # sknf = get_normal_form(gluing(get_variables(logical_formula)), '|')
    # logical_sknf = LogicalExpression(sknf + "|(a&c)")
    # truth_table = get_truth_table(logical_sknf)
    # for i in truth_table:
    #     print(i)
    
