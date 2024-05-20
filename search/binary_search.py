def binary_search(array: list[int], value: int) -> int:
    """
    This binary search assumes ascending order
    """
    if len(array) == 0:
        return -1
    
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right)//2
        current_value = array[middle] 
        if current_value == value:
            return middle
        if current_value > value:
            right = middle -1
        else:
            left = middle + 1

    return -1

lst = [i for i in range(0,100,2)]
print("index of 2 should be 1: ", binary_search(lst, 2))
print("index of 5 should be -1: ", binary_search(lst, 5))
print("index of 90 should be 45: ", binary_search(lst, 90))