import random

# Note
# XOR truth table
# A B   Y
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 0

# CRC generator polynomial dictionary
CRC_Dictionary = {
    'CRC-32': 'x ** 32 + x ** 26 + x ** 23 + x ** 22 + x ** 16 + x ** 12 + x ** 11 + x ** 10 + x ** 8 + x ** 7 + x ** 5 + x ** 4 + x ** 2 + x + 1',
    'CRC-24': 'x ** 24 + x ** 23 + x ** 14 + x ** 12 + x ** 8 + 1',
    'CRC-16': 'x ** 16 + x ** 15 + x ** 2 + 1',
    'Reversed CRC-16': 'x ** 16 + x ** 14 + x + 1',
    'CRC-8': 'x ** 8 + x ** 7 + x ** 6 + x ** 4 + x ** 2 + 1',
    'CRC-4': 'x ** 4 + x ** 3 + x ** 2 + x + 1'
}

# ---------------- # Function section # ---------------- #

# ---------------- # End of Helper Functions # ---------------- #


# Check if the input is bit string or not
def isBitString(input):
    for i in input:
        if i != "1" and i != "0":
            return False
    return True


# This function is to random binany number.
def random_dataword(n):
    binary = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        binary += temp
    return binary


# This function convert CRC polinomial to binary.
def CRC_PolynomialToBinary(CRC_method):
    polinomial = CRC_Dictionary.get(CRC_method)
    return bin(eval(polinomial.replace('x', '2')))[2:]


# This function is to generate the parity bits for the data word.
def divisionProcess(a, b):

    compared = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            compared.append('0')
        else:
            compared.append('1')

    return ''.join(compared)


# This function is using as a helper function for the division process.
def mod2div(dividend, divisor):

    xorBits = len(divisor)
    temp = dividend[0: xorBits]

    # print("Dividend", dividend, "First initial", temp, " and xorBits", xorBits)                   # DEBUG

    while xorBits < len(dividend):

        if temp[0] == '1':

            #     print("Calculation")
            #     print(temp + "\n" + divisor + "\n" +                                              # DEBUG
            #           ('0' + divisionProcess(divisor, temp)))

            temp = divisionProcess(divisor, temp) + dividend[xorBits]

        else:

            #     print("Calculation")
            #     print(temp + "\n" + divisor + "\n" +                                              # DEBUG
            #           ('0' + divisionProcess('0' * xorBits, temp)))

            temp = divisionProcess('0' * xorBits, temp) + dividend[xorBits]

        xorBits += 1

    # print("######## left n bits #########")                                                       # DEBUG

    if temp[0] == '1':

        temp = divisionProcess(divisor, temp)

        # print("Now temp is : ", temp)                                                             # DEBUG
    else:

        temp = divisionProcess('0' * xorBits, temp)

        # print("Now temp is : ", temp)                                                             # DEBUG

    checkword = temp

    return checkword


# ---------------- # End of Helper Functions # ---------------- #


# This function calculates the redundancy bit(s) for the dataword and output the codeword for CRC.
def CRC_gen(dataword, word_size, CRC_type):

    # Check if the input is a binary string
    #if not isBitString(codeword):
        #print("Error: Input is not a binary string")
        #return

    # Check if the word size is bigger than the key size
    if word_size < 5 and len(dataword) < word_size:
        print("Error: Word size is too small")
        return

    # Convert the CRC polinomial format "CRC-~" to binary
    key = CRC_PolynomialToBinary(CRC_type)
    key_size = len(key)
    extened_dataword = dataword + '0' * (key_size - 1)
    remainder = mod2div(extened_dataword, key)

    # Connect remainder to the dataword
    codeword = dataword + remainder

    print("Our original dataword :", dataword)
    print("Remainder : ", remainder)
    print("Encoded Data (Data + Remainder) : ", codeword)

    return codeword


# This function verifies the CRC codeword.
def CRC_check(codeword, CRC_type):

    # Check if the input is a binary string
    #if not isBitString(codeword):
        #print("Error: Input is not a binary string")
        #return

    # Convert the CRC polinomial format "CRC-~" to binary
    key = CRC_PolynomialToBinary(CRC_type)
    key_size = len(key)
    word_size = len(codeword)

    # Check if the word size is bigger than the key size
    if word_size < 5 and len(dataword) < word_size:
        print("Error: Word size is too small")
        return

    # Connect remainder to the dataword
    remainder = mod2div(codeword, key)

    if remainder.count("1") >= 1:
        return "Codeword: " + codeword + "\n Remainder: " + remainder + "\n Error: CRC check failed"
    else:
        return "Codeword: " + codeword + "\n Remainder: " + remainder + "\n Error: CRC check passed"


# ---------------- # End Function section # ---------------- #


# ---------------- # Main section # ---------------- #

# ---------------- Self specify dataword ---------------- #

dataword = "110101011"

# ---------------- Random dataword generatored ---------------- #

Num_of_bits = 6
# dataword = random_dataword(Num_of_bits)

CRC_type = "CRC-4"

codeword = CRC_gen(dataword, len(dataword), CRC_type)
print("# ---------------- Validation ---------------- #")
valid = CRC_check(codeword, CRC_type)
print(valid)

####################### End Main section ######################
