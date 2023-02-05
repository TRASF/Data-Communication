import random
# ---------------- # Function section # ---------------- #

# ---------------- # Helper Functions # ---------------- #

# This function generates the random data word
def random_dataword(n):
    binary = ""
    for i in range(n):
        temp = str(random.randint(0, 1))
        binary += temp
    return binary


# Use to spilt one string to array of string --> ref https://www.delftstack.com/howto/python/python-split-list-into-chunks/
def Chunksdata(data, size):
    return [data[i:i+size] for i in range(0, len(data), size)]


# Use to sum all data in binary number --> ref https://www.programiz.com/python-programming/methods/built-in/bin
def Summation(data):
    sum = 0
    for i in data:
        sum += int(i, 2)
    return bin(sum).replace("0b", "")

# ---------------- # End of Helper Functions # ---------------- #


def Checksum_gen(dataword, word_size, num_blocks):

    Numbits = int(word_size/num_blocks)

    # spilt dataword
    chunks = Chunksdata(dataword, Numbits)

    # sum of all dataword
    binarysum = Summation(chunks)

    # check to fill 0 on beginning of array
    while(len(binarysum) % Numbits != 0):

        binarysum = "0" + binarysum

    wapped = Chunksdata(binarysum, Numbits)
    wappedsum = Summation(wapped)

    while(len(wappedsum) % Numbits != 0):

        wappedsum = "0" + wappedsum

    # convert 0 to 1 and 1 to 0
    checksum = ''

    for i in range(len(wappedsum)):

        if(wappedsum[i] == "1"):
            checksum += '0'
        else:
            checksum += '1'

    return dataword + checksum


# This function verifies the Checksum codeword
def Checksum_check(codeword, word_size, num_blocks):

    Numbits = int(word_size/num_blocks)

    # spilt codeword
    chunks = Chunksdata(codeword, Numbits)

    # summation
    binarysum = Summation(chunks)

    # check to fill 0 on beginning of array
    while(len(binarysum) % Numbits != 0):

        binarysum = "0" + binarysum

    wapped = Chunksdata(binarysum, Numbits)
    wappedadd = Summation(wapped)

    # check if all in wappedadd are 1
    count = 0
    for i in range(len(wappedadd)):

        if(wappedadd[i] == "1"):
            count += 1

    # if all is 1 return 1(pass) otherwise return 0(fail)
    if(count == len(wappedadd)):
        return 1
    else:
        return 0

# ---------------- # End Function section # ---------------- #

# ---------------- # Main section # ---------------- #
# Check if this function encodes the dataword correctly
n = 10
dataword1 = []

for i in range(n):
    dataword1.append(random_dataword(16))

for i in dataword1:
    codeword1 = Checksum_gen(i, len(i), 4)
    validity1 = Checksum_check(codeword1, len(codeword1), 5)
    print(codeword1, validity1)




# ---------------- # End Main section # ---------------- #
