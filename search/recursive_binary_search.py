def binary_search(array: list[int], value: int) -> int:
    return recursive_binary_search(array, value, 0, len(array)-1)


def recursive_binary_search(array: list[int], value: int, start: int, end: int) -> int:
    # base cases
    if start > end:
        return -1
    middle = (start+end)//2
    if array[middle] == value:
        return middle
    # recursive cases
    elif array[middle] > value:
        return recursive_binary_search(array, value, start, middle-1)
    else:
        return recursive_binary_search(array, value, middle+1, end)
    
lst = [i for i in range(0,100,2)]
print("index of 2 should be 1: ", binary_search(lst, 2))
print("index of 5 should be -1: ", binary_search(lst, 5))
print("index of 90 should be 45: ", binary_search(lst, 90))