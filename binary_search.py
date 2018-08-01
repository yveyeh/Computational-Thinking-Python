# binary search (array of numbers) in python

def binary_search(list_object, element):
    first = 0
    last = len(list_object)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list_object[midpoint] == element:
            found = True
        else:
            if element < list_object[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

values = [0, 1, 2, 8, 13, 17, 18, 19, 21, 25, 27, 28, 29, 30, 32, 42, 45]
print(binary_search(values, 3))
print(binary_search(values, 13))
print(binary_search(values, 46))


# recursive way (still in python)

# def binary_search(list_object, element):
#     if len(list_object) == 0:
#         return False
#     else:
#         midpoint = len(list_object) // 2
#         if list_object[midpoint] == element:
#             return True
#         else:
#             if element < list_object[midpoint]:
#                 return binary_search(list_object[:midpoint], element)
#             else:
#                 return binary_search(list_object[midpoint+1:], element)

# values = [0, 1, 2, 8, 13, 17, 18, 19, 21, 25, 27, 28, 29, 30, 32, 42, 45]
# print(binary_search(values, 4))
# print(binary_search(values, 25))

