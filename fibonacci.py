def printSimpleFibonacci(limit):
    """Returns a listed fibonacci sequence up to the limit specified"""
    previous, current, sequence = 0, 1, []

    for number in range(limit):

        if number == 1 or number == 0:
            sequence.append(number)

        if number == current + previous:
            previous = current
            current = number
            sequence.append(current)

    return sequence



# fib = printSimpleFibonacci(45)
# print(fib)
