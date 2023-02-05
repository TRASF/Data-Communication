import random

# ---------------- # Functions Section # ---------------- #

# ---------------- # Helper Functions && Error Check # ---------------- #


# Check if the input is bit string or not
def isBitString(input):
    for i in input:
        if i != "1" and i != "0":
            return False
    return True


# This function generates the random data word
def random_dataword(n):
    binary = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        binary += temp
    return binary


# This function checks the parity bits and return the parity bit
def parityCheck(word):
    count = 0
    for data in word:
        if data == '1':
            count += 1

    if count % 2 == 0:
        return '0'
    else:
        return '1'

# ---------------- # End of Helper Functions && Error Check # ---------------- #


# This function calculates the redundancy bit(s) for the dataword and output the codeword for Hamming code
def Hamming_gen(dataword):

    # Check if the input is a binary string
    if not isBitString(dataword):
        print("Error: Input is not a binary string")
        return

    size = len(dataword)
    redundant_bits = 0

    # Find the redundant bits
    while 2 ** redundant_bits - (redundant_bits - 1) < size:
        redundant_bits += 1

    # Convert to list then reverse for insertion empty slot and compute parity bits
    extended_dataword = list(dataword)
    list.reverse(extended_dataword)

    # insert empty slot to every 2 ^ index - 1
    for index in range(redundant_bits):
        extended_dataword.insert(2 ** index - 1, 'X')

    # compute parity bits
    for index in range(redundant_bits):
        checkSequence = []

        # Loop for interval checking
        for skip in range(2 ** index):

            # Extend to use as interval checking for parity bits in the extended dataword
            # start parameter will run [0:size-1] and jump parameter will run as interval [2, 4, 8, 16] for parity bit coverage
            checkSequence.extend(
                extended_dataword[2 ** index + (skip-1)::2 ** (index + 1)])

            # print("firstParams", 2 ** index + (skip-1), "SecondParams", 2 ** (index + 1),   # DEBUG
            #       "Data", extended_dataword[2 ** index + (skip-1)::2 ** (index + 1)])

        # convert to string for parity check
        extended_dataword[2 ** index - 1] = parityCheck("".join(checkSequence))

    # reverse back to original order
    list.reverse(extended_dataword)

    print("Hamming Code:", "".join(extended_dataword))

    return extended_dataword


# This function verifies the Hamming codeword and report the location of error for the case of single bit error
def Hamming_check(codeword):

    # Check if the input is a binary string
    if not isBitString(codeword):
        print("Error: Input is not a binary string")
        return

    size = len(codeword)
    redundant_bits = 0

    # Find the redundant bits
    while 2 ** redundant_bits - (redundant_bits - 1) < size:
        redundant_bits += 1

    # Convert to list then reverse for insertion empty slot and compute parity bits
    extended_codeword = list(codeword)
    list.reverse(extended_codeword)

    caugth_error = ''

    for i in range(redundant_bits):
        checkSequence = []

        # Loop for interval checking
        for skip in range(2 ** i):

            # Extend to use as interval checking for parity bits in the extended dataword
            # start parameter will run [0:size-1] and jump parameter will run as interval [2, 4, 8, 16] for parity bit coverage
            checkSequence.extend(
                extended_codeword[2 ** i + (skip - 1)::2 ** (i + 1)])

            # print("firstParams", 2 ** i + (skip-1), "SecondParams", 2 ** (i + 1),   # DEBUG
            #       "Data", extended_codeword[2 ** i + (skip-1)::2 ** (i + 1)])

        # convert to string for parity check
        if parityCheck("".join(checkSequence)) == '1':
            caugth_error += "1"
        else:
            caugth_error += "0"

    # Check if there is error or not
    if int(caugth_error, 2) == 0:
        print("No error detected")
    else:
        print("Error detected:", len(caugth_error), "bits", "From left side")

    # reverse back to original order
    list.reverse(extended_codeword)

    return extended_codeword


# ---------------- # End of Functions Section # ---------------- #


# ---------------- # Main Section # ---------------- #



codeword = Hamming_gen(random_dataword(7))
Hamming_check(codeword)



# ---------------- # End of Main Section # ---------------- #
