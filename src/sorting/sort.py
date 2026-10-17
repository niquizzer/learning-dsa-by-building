def find_smallest_index(arr:list[int]) -> int:
    smallest_index = 0
    smallest = arr[0]

    for i,v in enumerate(arr):
        if v < smallest:
            smallest = v
            smallest_index = i
    
    return smallest_index

def sort_descending(arr:list[int]) -> list[int]:
    """ Sorts integer list descending.

    Args:
        lst(list[int]): integer list.

    Returns:
        list(int): is a new list with values
        sorted in descending order.
    """
    result = []

    if arr == []:
        return "Empty list"
    
    for x in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        result.append(arr.pop(smallest_index))

    return [x for x in reversed(list(result))]