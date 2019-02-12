def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if input_array[midpoint] == value:
            found = True
        else:
            if input_array[midpoint] < value:
                first = midpoint + 1
            else:
                last = midpoint - 1
        
    return found

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))