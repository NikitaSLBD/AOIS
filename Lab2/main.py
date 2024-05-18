from logical_expression import LogicalExpression
from truth_table import get_truth_table
from forms import index_form, build_sdnf, build_sknf

logical_formula = LogicalExpression(input("Enter your logical expretion: "))

print("Truth table:\n")
for i in get_truth_table(logical_formula):
    print(i)

print("SDNF:")
print(build_sdnf(get_truth_table(logical_formula)))
print("SKNF:")
print(build_sknf(get_truth_table(logical_formula)))
print("Index form:")
print(index_form(get_truth_table(logical_formula)))
