from numbertranslator import dec_to_bin_sign, bin_sign_to_dec

def number_to_bin_int_part(number) -> str:
    return dec_to_bin_sign(int(number))


def number_to_bin_fraction_part(number: float) -> str:

    bin_fraction_part = ""
    fraction_part = abs(number - int(number))

    for i in range(1, 18):
        if fraction_part - 2 ** (-i) >= 0:

            fraction_part -= 2 ** (-i)
            bin_fraction_part += "1"

        else: bin_fraction_part += "0"

    fraction_part = bin_fraction_part.zfill(17)

    return bin_fraction_part

# def number_to_bin_fraction_part(number) -> str:
#     return dec_to_bin_sign((abs(number - int(number)) * 100000))
                           
def parts_to_number(bin_int_part: str, bin_fraction_part: str) -> float:
    if bin_int_part[0] != "1":
        return bin_sign_to_dec(bin_int_part) + (bin_sign_to_dec(bin_fraction_part) / 100000)
    else: return bin_sign_to_dec(bin_int_part) - (bin_sign_to_dec(bin_fraction_part) / 100000)

class FixDotNumber:

    def __init__(self, value1, value2: str=None):

        if not value2:
            self._number: float = value1
            self._bin_int_part: str = number_to_bin_int_part(self._number)
            self._bin_fraction_part: str = number_to_bin_fraction_part(self._number)
        elif value2:
            self._bin_int_part: str = value1
            self._bin_fraction_part: str = value2
            self._number: float = parts_to_number(self._bin_int_part, self._bin_fraction_part)

    def __str__(self):
        return str({"Decimal fraction": self._number, "Bin int": self._bin_int_part, 
                    "Bin fraction": self._bin_fraction_part}) 