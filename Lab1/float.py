from numbertranslator import bin_sign_to_dec, dec_to_bin_sign

def evaluate_mantissa(bin_mantissa: str) -> float:

    mantissa = 1

    for i in range(len(bin_mantissa) - 1, -1, -1):
        mantissa += 2 ** -(i + 1) * int(bin_mantissa[i])
    
    return mantissa

def evaluate_bin_mantissa(mantissa: float) -> str:

    bin_mantissa = ""

    for i in range(1, 24):
        if mantissa - 2 ** (-i) >= 0:

            mantissa -= 2 ** (-i)
            bin_mantissa += "1"

        else: bin_mantissa += "0"

    bin_mantissa = bin_mantissa.zfill(23)

    return bin_mantissa

class Float:

    def __init__(self, number: float=None, sign: bool=False, 
                 bin_exponent: str=None, bin_mantissa: str=None):

        if number is None:

            self.__sign: bool = sign
            self.__exponent: str = bin_exponent.zfill(8)
            self.__mantissa: str = bin_mantissa.zfill(23)

            if list(filter(lambda bit: bit == "1", bin_exponent + bin_mantissa )) == []:
                self.__value = 0
                return

            if not sign:

                self.__value: float = evaluate_mantissa(bin_mantissa) * 2 ** \
                                    (bin_sign_to_dec('0' + bin_exponent) - 127)
            
            else: self.__value: float = -evaluate_mantissa(bin_mantissa) * 2 ** \
                                    (bin_sign_to_dec('0' + bin_exponent) - 127)

        elif number or number == 0:

            self.__value = number
            self.__sign: bool = bool(number < 0)

            if not number:

                self.__exponent = "".zfill(8)
                self.__mantissa = "".zfill(23)
                return

            for i in range (0, 257):
                if 1 <= (number / 2 ** i) < 2: 
                    self.__exponent = dec_to_bin_sign(i + 127)[-8:]
                    self.__mantissa = evaluate_bin_mantissa((number - 2 ** i) / 2 ** i)


    def __str__(self):

        bin_representation = str(int(self.__sign)) + self.__exponent + self.__mantissa
        return str({"Value": self.__value, "Bin": bin_representation})
    

    def get_exponent(self) -> str: return self.__exponent
    def get_mantissa(self) -> str: return self.__mantissa
    def get_value(self) -> float: return self.__value





        
        