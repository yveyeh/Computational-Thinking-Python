# Function that takes in a list and returns a list
def printList(data):

    result = []

    for x in data:

        if type(x) is int or type(x) is str:
            result.append(x)
        else:
            result.extend(printList(x))
            
    return(result)


# newList = printList(["This is a string", 1, 2, [3], [4, [5, 6]], 7, 8, "[9, 10]"])
# print(newList)