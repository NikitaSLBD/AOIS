def dec_to_bin_sign(dec: int) -> str:

        bin_sign = ""
        positive_number = abs(dec)

        while (positive_number != 1 and positive_number):
            bit = str(positive_number % 2)
            positive_number //= 2
            bin_sign += bit
        else: bin_sign += str(positive_number)

        bin_sign = bin_sign[::-1]
        bin_sign = bin_sign.zfill(31)

        bin_sign = "0" + bin_sign if dec >= 0 else "1" + bin_sign
        return bin_sign

def bin_sign_to_dec(bin_sign: str) -> int:

    dec = 0

    for i in range(1, len(bin_sign)):
        dec += 2 ** (-i + len(bin_sign) - 1) * int(bin_sign[i]) 
    
    if bin_sign[0] != "0" and len(bin_sign) > 16: return -dec
    else: return dec