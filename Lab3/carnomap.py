from forms import bin_sign_to_dec
from truth_table import values_generator

import re

def carno_map(formula_values, carno_values) -> dict[str: int]:

    carno_map = []

    for value in carno_values:
        carno_map.append({value: formula_values[bin_sign_to_dec('0' + value)]})
    
    return carno_map 

def build_carno_map(truth_table):

    formula_values = list(map(lambda a: int(str(a[1])[-2]), truth_table))
    values_count = len(formula_values)

    match values_count:
        case 0: return None
        case 2: return {'0': formula_values[0], '1': formula_values[1]}
        case 4: return carno_map(formula_values, ['00', '01', '10', '11'])
        case 8: 
            values = ['000', '001', '011', '010', 
                      '100', '101', '111', '110']
            
            return carno_map(formula_values, values)
        case 16: 
            values = ['0000', '0001', '0011', '0010', 
                      '0100', '0101', '0111', '0110', 
                      '1100', '1101', '1111', '1110',
                      '1000', '1001', '1011', '1010']
            
            return carno_map(formula_values, values)
        case 32:
            values = ['00000', '00001', '00011', '00010', '00110', '00111', '00101', '00100',
                      '01000', '01001', '01011', '01010', '01110', '01111', '01101', '01100',
                      '11000', '11001', '11011', '11010', '11110', '11111', '11101', '11100',
                      '10000', '10001', '10011', '10010', '10110', '10111', '10101', '10100']
            
            return carno_map(formula_values, values)

def print_carno_map(carno_map: list[dict[str: int]]):

    x, y = 0, 0

    if len(carno_map) < 8: print(carno_map)
    elif len(carno_map) == 8: x, y = 4, 2
    elif len(carno_map) == 16: x, y = 4, 4
    else: x, y = 8, 4

    for i in range(y):
        print()
        for j in range(x): 
            print(carno_map[j + i * y], end='')

    

        





    
