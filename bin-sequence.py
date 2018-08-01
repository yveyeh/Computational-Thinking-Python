
def getBinary(number): # returns the exact  binary of given number
    return bin(number)[2:]

def getLongestSequence(binary):

    currentNumber = 0
    definiteNumber = 0

    for i in range(len(binary)):

        if (binary[i] == '0'):
            currentNumber += 1
            continue
        
        if (binary[i] == '1'):
            if (definiteNumber < currentNumber):
                definiteNumber = currentNumber
            currentNumber = 0

    return definiteNumber


# binaryNumber = getBinary(99999999)
# longestSequenceNumber = getLongestSequence(binaryNumber)
# print(longestSequenceNumber)
