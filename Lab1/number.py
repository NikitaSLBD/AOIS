from numbertranslator import dec_to_bin_sign, bin_sign_to_dec

def logical_negation(bit: chr) -> chr:
    return "0" if bit != "0" else "1"

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


def bin_ones_complement(bin_sign: str) -> str:

    if bin_sign[0] != "0": 
        return bin_sign[0] + "".join(map(logical_negation, bin_sign[1:])) 
    else: return bin_sign

def bin_twos_complement(bin_sign: str) -> str:   

    one_bin = "".zfill(len(bin_sign) - 1) + "1"

    if bin_sign[0] != "0":
        return "1" + adding(bin_ones_complement(bin_sign), one_bin) 
    else: return bin_sign

class Number:

    def __init__(self, value):

        if isinstance(value, int):
            self._dec = value
            self._bin_sign = dec_to_bin_sign(self._dec)
        elif isinstance(value, str):
            self._bin_sign = value
            self._dec = bin_sign_to_dec(self._bin_sign)
        elif value == "1" + "0" * 31:
            self._dec = 0
            self._bin_sign = "0" * 32
        else: raise TypeError

        self._bin_ones_complement = bin_ones_complement(self._bin_sign)
        self._bin_twos_complement = bin_twos_complement(self._bin_sign)

    def __str__(self):

        return str({"Decimal": self._dec, "Binary with sign": self._bin_sign,
                         "Binary one`s complement": self._bin_ones_complement,
                         "Binary two`s complement": self._bin_twos_complement})
    
    
    
    def get_dec(self) -> int: return self._dec
    def get_bin_sign(self) -> str: return self._bin_sign
    def get_bin_ones_complement(self) -> str: return self._bin_ones_complement
    def get_bin_twos_complement(self) -> str: return self._bin_twos_complement
    
    

    