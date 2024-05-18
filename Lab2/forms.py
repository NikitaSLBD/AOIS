def bin_sign_to_dec(bin_sign: str) -> int:

    dec = 0

    for i in range(len(bin_sign)):
        dec += 2 ** (-i + len(bin_sign) - 1) * int(bin_sign[i]) 
    
    if bin_sign[0] != "0" and len(bin_sign) > 16: return -dec
    else: return dec

def index_form(truth_table):

    index = "".join(list(map(lambda a: str(a[1])[-2], truth_table)))
    return {bin_sign_to_dec(index): index}

def build_sdnf(truth_table):

    disjuncts = []
    for interpr in truth_table:
        if str(interpr[1])[-2] == '1':
            disjuncts.append(interpr[0])

    sdnf = ""
    number_sdnf = []

    for j, disj in enumerate(disjuncts):
        
        sdnf += '('
        values = list(map(lambda a: str(a), disj.values()))
        number_sdnf.append(bin_sign_to_dec("".join(values)))

        for i, key in enumerate(disj): 
            sdnf += key if disj[key] else '!' + key
            if i + 1 != len(disj): sdnf += '&' 

        if j + 1 != len(disjuncts): sdnf += ")|"
        else: sdnf += ')'

    return {sdnf: number_sdnf}

def build_sknf(truth_table):

    conjuncts = []
    for interpr in truth_table:
        if str(interpr[1])[-2] == '0':
            conjuncts.append(interpr[0])

    sknf = ""
    number_sknf = []

    for j, conj in enumerate(conjuncts):
        
        sknf += '('
        values = list(map(lambda a: str(a), conj.values()))
        number_sknf.append(bin_sign_to_dec("".join(values)))

        for i, key in enumerate(conj): 
            sknf += '!' + key if conj[key] else key
            if i + 1 != len(conj): sknf += '|' 

        sknf += ")&" if (j + 1 != len(conjuncts)) else ')'
        

    return {sknf: number_sknf}

def get_normal_form(variables: list[set], form_type: chr):

    sknf = ''
    operations = ['|', '&'] if form_type != '|' else ['&', '|']

    for i, conjuct in enumerate(variables):

        sknf += '('

        while conjuct:
            if len(conjuct) != 1: sknf += conjuct.pop() + f'{operations[0]}' 
            else: sknf += conjuct.pop()

        sknf += f"){operations[1]}" if (i + 1 != len(variables)) else ')'

    return sknf




