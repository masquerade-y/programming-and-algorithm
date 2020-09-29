"""A function to achieve iterative binary search.
Assume the list only has distinct elements,
i.e. no repeated values, and elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """The function takes two inputs:
    a Python list to search through, 
    and the value you're searching for."""
    low = 0
    high = len(input_array) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] < value:
            low = mid + 1
        elif input_array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

# test
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
