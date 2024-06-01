from minimization import calculate_minimization, table_minimization, carno_minimization
from carnomap import build_carno_map, print_carno_map
from truth_table import  get_truth_table
from logical_expression import LogicalExpression

if __name__ == "__main__":

    logical_formula = input("Enter sknf or sdnf: ")
    carno_map = build_carno_map(get_truth_table(LogicalExpression(logical_formula)))

    print("\nCalculation method:")
    print(calculate_minimization(logical_formula))
    print("\nTable-calculation method:")
    print(table_minimization(logical_formula))
    print("\nCarno method:")
    print("Carno Map:")
    print_carno_map(carno_map)
    print('\nMinimize function:')
    print(carno_minimization(logical_formula))
