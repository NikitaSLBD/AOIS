from number import Number, adding, bin_ones_complement, bin_twos_complement
from fixdotnumber import FixDotNumber
from float import Float, evaluate_mantissa, evaluate_bin_mantissa
from numbertranslator import bin_sign_to_dec, dec_to_bin_sign


def plus(number1: Number, number2: Number) -> Number:

    bin_sum = ""

    if number1.get_bin_sign()[0] == number2.get_bin_sign()[0]:

        bin_sum = number1.get_bin_sign()[0] + \
                  adding(number1.get_bin_sign(), number2.get_bin_sign())  
        
    elif number1.get_bin_sign()[0] != "0":

        bin_sum = adding(number1.get_bin_twos_complement(), number2.get_bin_sign())
            
        if abs(number1.get_dec()) >= abs(number2.get_dec()):
            bin_sum = "1" + bin_sum
        else: bin_sum = "0" + bin_sum

        if bin_sum[0] == "1":
            bin_sum = bin_twos_complement(bin_sum)
    
    else: 

        bin_sum = adding(number1.get_bin_sign(), number2.get_bin_twos_complement())
        
        if abs(number1.get_dec()) >= abs(number2.get_dec()):
            bin_sum = "0" + bin_sum
        else: bin_sum = "1" + bin_sum         

        if bin_sum[0] == "1":
            bin_sum = bin_twos_complement(bin_sum)   
            
    return Number(bin_sum)
        

def minus(number1: Number, number2: Number) -> Number:

    bin_dif = ""

    if number1.get_bin_sign()[0] != number2.get_bin_sign()[0]:

        if number1.get_bin_sign()[0] != "0":
            bin_dif = "1" + adding(number1.get_bin_sign(), number2.get_bin_sign())
        else:
            bin_dif = "0" + adding(number1.get_bin_sign(), number2.get_bin_sign())

    elif number1.get_bin_sign()[0] != "0":

        bin_dif = adding(number1.get_bin_twos_complement(), number2.get_bin_sign())
            
        if abs(number1.get_dec()) >= abs(number2.get_dec()):
            bin_dif = "1" + bin_dif
        else: bin_dif = "0" + bin_dif

        if bin_dif[0] == "1":
            bin_dif = bin_twos_complement(bin_dif)
    
    else: 

        number2 = Number(-number2.get_dec())
        bin_dif = adding(number1.get_bin_sign(), number2.get_bin_twos_complement())

        if abs(number1.get_dec()) >= abs(number2.get_dec()):
            bin_dif = "0" + bin_dif
        else: bin_dif = "1" + bin_dif 

        if bin_dif[0] == "1":
            bin_dif = bin_twos_complement(bin_dif)

        

    return Number(bin_dif)

def increasing(bin1: str, bin2: str) -> str:
  
    buf_result = ""

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    result = "".zfill(max_len - 1)

    for i in range(len(bin2) - 1, 1, -1):

        buf_result = buf_result.zfill(-i + 31)

        for j in range(len(bin1) - 1, 1, -1):

            if (bin2[i] == "1" and bin1[j] == "1"):
                buf_result = "1" + buf_result
            else: buf_result = "0" + buf_result

        result = adding(result, buf_result[-i + 31:])
        buf_result = ""

    return result.zfill(max_len - 1)

def multiplication(number1: Number, number2: Number) -> Number:

    bin_product = ""

    if number1.get_bin_sign()[0] == number2.get_bin_sign()[0]:
        bin_product = "0" + increasing(number1.get_bin_sign(), number2.get_bin_sign())
    else: bin_product = "1" + increasing(number1.get_bin_sign(), number2.get_bin_sign())

    return Number(bin_product)

def division(number1: Number, number2: Number) -> FixDotNumber:
    
    bin_product = ""


    if number1.get_bin_sign()[0] == number2.get_bin_sign()[0]:

        number1 = Number(abs(number1.get_dec()))
        number2 = Number(int((1 / abs(number2.get_dec())) % 1 * 1_000_000))
        bin_product = "0" + increasing(number1.get_bin_sign(), number2.get_bin_sign())
    else: 
        
        number1 = Number(abs(number1.get_dec()))
        number2 = Number(int((1 / abs(number2.get_dec())) % 1 * 1_000_000))
        bin_product = "0" + increasing(number1.get_bin_sign(), number2.get_bin_sign())

    product = bin_sign_to_dec(bin_product) / 1_000_000

    return FixDotNumber(product)

def biggest_bin_number(bin1: str, bin2: str) -> str:

    for i in range(len(bin1)):

        if bin1[i] == "1" and bin2[i] == "0":
            return bin1
        
        elif bin1[i] == "0" and bin2[i] == "1":
            return bin2
        
    return None
                
def adding_mantisses(mantiss1: str, mantiss2: str) -> str:
    result = ""
    carry = False

    max_len = max(len(mantiss1), len(mantiss2))
    mantiss1 = mantiss1.zfill(max_len)
    mantiss2 = mantiss2.zfill(max_len)

    for i in range(max_len - 1, 0, -1):

        if (mantiss1[i] == "1" and mantiss2[i] == "1"):
            
            if carry:
                result = "1" + result
            else:
                result = "0" + result
                carry = True
                continue

        elif (mantiss1[i] == "0" and mantiss2[i] == "0"):

            if carry:
                result = "1" + result
                carry = False
            else: result = "0" + result 

        else:

            if carry:
                result = "0" + result
            else: result = "1" + result 

    if carry: result = "1" + result

    result = result.zfill(31)

    return result

def calculate_mantisses_sum(exponent1: str, mantissa1: str, exponent2: str, mantissa2: str):
    
    exponent_sum = biggest_bin_number(exponent1, exponent2)
    mantissa1 = "1" + mantissa1
    mantissa2 = "1" + mantissa2
    if exponent_sum:

        exponent_diff = bin_sign_to_dec(exponent1) - bin_sign_to_dec(exponent2)
        
        if exponent_diff > 0: mantissa2 = mantissa2.zfill(24 + exponent_diff)
        else: mantissa1 = mantissa1.zfill(24 - exponent_diff)

    elif not exponent_sum: exponent_sum = exponent1

    max_len = max(len(mantissa1), len(mantissa2))
    len_diff = len(mantissa1) - len(mantissa2)

    if len_diff > 0: mantissa2 = mantissa2 + "0" * len_diff
    else: mantissa1 = mantissa1 + "0" * -len_diff

    mantiss_sum = adding_mantisses("0" + mantissa1, "0" + mantissa2)[-max_len - 1:]

    if mantiss_sum[0] == "1":
        exponent_sum = adding("0" + exponent_sum, "1".zfill(9))[-8:]
        mantiss_sum = mantiss_sum[1:24]
    else: mantiss_sum = mantiss_sum[2:25]

    return mantiss_sum, exponent_sum


def float_plus(float1: Float, float2: Float) -> Float:

    mantiss_sum, exponent_sum = calculate_mantisses_sum(float1.get_exponent(), float1.get_mantissa(),
                                                        float2.get_exponent(), float2.get_mantissa())

    return Float(bin_exponent=exponent_sum, bin_mantissa=mantiss_sum)

    
if __name__ == "__main__":
    pass
