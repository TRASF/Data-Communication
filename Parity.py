from collections import Counter
import random
import numpy as np

################################# Functions section #################################


############# Error Check && Helper Function #############


# Check if the input is bit string or not
def isBitString(input):
    for i in input:
        if i != "1" and i != "0":
            return False
    return True


# This function is used to check if the input is a valid parity codeword or not
def checkData(data, type):
    count = data.count("1")
    if count % 2 == 0 and type == "2D_even" or count % 2 == 1 and type == "2D_odd":
        return True
    else:
        return False


# This function is used to merge 2D array into string
def merge(codeword, word_size, array_size, space):
    actualBinary = ""
    for row in range(word_size):
        for col in range(array_size):
            actualBinary += codeword[row][col]
        if space:
            actualBinary += " "
    return actualBinary


# This function is used to random generate a data word
def random_dataword(n):
    binary = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        binary += temp
    return binary

# this function is used to random generate a data word


def random_2D_dataword(n, array_size):
    return random_dataword(n * array_size)


############# End Error Check && Helper Function #############


# This function calculates the redundancy bit(s) for the array of dataword and output an array of codeword.
def parity_genetator(dataword, word_size, parity_type, array_size):

    # Check if the input is a binary string
    if not isBitString(dataword):
        print("Error: Input is not a binary string")
        return
    # Case for odd parity and even parity
    if parity_type == "even" or parity_type == "odd":

        codeword = ""
        # Check if the input is a valid parity codeword or not
        if dataword.count("1") % 2 == 0 and parity_type == "even" or dataword.count("1") % 2 == 1 and parity_type == "odd":
            temp = dataword + "0"
            codeword += temp
        else:
            temp = dataword + "1"
            codeword += temp

        return codeword

    # Case for 2D even parity and 2D odd parity
    elif parity_type == "2D_even" or parity_type == "2D_odd":

        # Check if the input is a valid size of parity codeword or not
        if len(dataword) != (array_size * word_size):

            print(
                "Error: Array size is not equal to word size * array size")
            return

        else:

            for i in range(array_size):
                while len(dataword) < word_size:
                    dataword += "0"

        # Convert to list
        splitData = [char for char in dataword]

        # Reshape the list
        codeword = np.reshape(splitData, (word_size, array_size))

        # print(codeword)                                                                                   #DEBUG

        # Using for row parity check then transpose the array
        tempRow = [None] * word_size
        tempRow = np.reshape(tempRow, (word_size, 1))

        # Count '1' in the codeword
        for row in range(word_size):
            count = 0
            for i in codeword[row]:
                if i == "1":
                    count += 1

            # print(count, codeword[row])                                                                   #DEBUG

            # Check if the input is a valid parity codeword or not
            if count % 2 == 0 and parity_type == "2D_even" or count % 2 == 1 and parity_type == "2D_odd":

                # print("Insert 0")
                tempRow[row] = "0"

            else:

                # print("Insert 1")
                tempRow[row] = "1"

        # Add the parity bit to the codeword at the end of row [size + 1]
        extendedColumn = np.hstack((codeword, tempRow))
        array_size += 1

        # print("Extended column\n", extendedColumn)                                                        # DEBUG
        # print("Temp Row\n", tempRow)                                                                      # DEBUG

        # Remap the array for column parity check
        oneN = []
        for col in zip(*extendedColumn):
            oneN.append(col)

        # print("Remap ")                                                                                   # DEBUG
        # print_array(oneN)                                                                                 # DEBUG

        # Using for column parity check
        tempCol = [] * array_size

        for row in range(array_size - 1):

            count = oneN[row].count("1")

            # print(count, oneN[row])                                                                       # DEBUG

            # Check if the input is a valid parity codeword or not
            if count % 2 == 0 and parity_type == "2D_even" or count % 2 == 1 and parity_type == "2D_odd":

                # print("insert 0")                                                                         # DEBUG

                tempCol.append("0")

            else:

                # print("insert 1")                                                                         # DEBUG

                tempCol.append("1")

        # Using for check if the parity bit is correct or not
        count = tempCol.count("1")

        # Check if the input is a valid parity codeword or not
        if count % 2 == 0 and parity_type == "2D_even" or count % 2 == 1 and parity_type == "2D_odd":
            tempCol.append("0")
        else:
            tempCol.append("1")

        # Add the parity bit to the codeword at the end of column [size + 1]
        extendedRow = np.vstack((extendedColumn, tempCol))

        # print("Extended row\n", extendedRow)                                                              # DEBUG
        # print("Temp Col\n", tempCol)                                                                      # DEBUG

        word_size += 1

        # Convert array to string
        actualBinary = merge(extendedRow, word_size, array_size, False)
        BeautifulBinary = merge(extendedRow, word_size, array_size, True)

        # print("Row parity check:")                                                                        # DEBUG
        # print_array(codeword)                                                                             # DEBUG

        # print("Column parity check:")                                                                     # DEBUG
        # print_array(codeword)                                                                             # DEBUG

        return actualBinary, BeautifulBinary, word_size, array_size


# This function verifies the codeword
def parity_check(codeword, partity_type, array_size):

    # Check if the input is a binary string
    if not isBitString(dataword):
        print("Error: Input is not a binary string")
        return

    # Case for odd parity and even parity
    if parity_type == "odd" or parity_type == "even":

        # Check if the input is a valid parity codeword or not
        count = codeword.count("1")
        if count % 2 == 0 and parity_type == "even" or count % 2 == 1 and parity_type == "odd":

            print("Codeword is correct")
            return True

        else:

            print("Codeword is incorrect")
            return False

    # Case for 2D even parity and 2D odd parity
    elif parity_type == "2D_odd" or parity_type == "2D_even":

        sizes = array_size.split('x')
        rows = int(sizes[0]) + 1
        cols = int(sizes[1]) + 1

        # Check if the input is a valid size of parity codeword or not
        if (len(codeword) - codeword.count(' ')) != rows * cols:
            print("Error: Array size is not equal to word size * array size")
            return

        # Check if the input is a valid parity codeword or not
        check = "True"

        # For row parity check
        for row in range(rows):
            if not checkData(codeword[row*cols:row*cols+cols], parity_type):

                # print("Row", codeword[row*cols:row*cols+cols])                                                  # DEBUG

                check = "False"
                break

        # For column parity check
        for col in range(cols):

            if not checkData(codeword[col::cols], parity_type):

                # print("Col", codeword[col::cols])                                                               # DEBUG

                check = "False"
                break

        print("Type: " + partity_type + "\nValid: " + check)
    else:
        print("Invalid parity type")
        return


################################# End of Functions section ###########################

################################# Main section #######################################

# --------------- Variables --------------- #
# Size of the dataword
dataword_size = 5

# Size of an array
array_size = 3

# --------------- 1D array --------------- #

### --------------- Uncomment to use --------------- ###

### ----------------- 1D even parity ----------------- ###

# parity_type = "even"

### 1D even array random dataword ###
# dataword = random_dataword(dataword_size)

### 1D even array self specify dataword ###
# dataword  "11001011"

### ----------------- 1D odd parity ----------------- ###

parity_type = "odd"

### 1D odd array random dataword ###
dataword = random_dataword(dataword_size)

### 1D odd array self specify dataword ###
# dataword = "11001011"

# --------------- 2D array --------------- #

### --------------- Uncomment to use --------------- ###

### --------------- 2D even array --------------- ###

# parity_type = "2D_even"

### 2D even array random dataword ###
# dataword = random_2D_dataword(dataword_size, array_size)

### 2D even array self specify dataword ###
# dataword = "110010110"

### ---------------- 2D odd array --------------- ###

# parity_type = "2D_odd"

### 2D odd array random dataword ###
# dataword = random_2D_dataword(dataword_size, array_size)

### 2D odd array self specify dataword ###
# dataword = "110010110"

# --------------- End of variables --------------- #

print("Original dataword: " + dataword)

if parity_type == "odd" or parity_type == "even":

    codeword = parity_genetator(dataword, dataword_size, parity_type, 0)
    print("Now our Codeword is: ", codeword)

elif parity_type == "2D_even" or parity_type == "2D_odd":

    codeword, beautifulBinary, newWordSize, newArraySize = parity_genetator(
        dataword, dataword_size, parity_type, array_size)
    print("Now our Codeword is: ", beautifulBinary)

print("\n# ---------------- # Parity Check # ---------------- #\n")

if parity_type == "odd" or parity_type == "even":

    parity_check(codeword, parity_type, -1)

else:

    sizeForcheck = str(dataword_size) + 'x' + str(array_size)
    parity_check(codeword, parity_type, sizeForcheck)


################################# End Main section ##################################
