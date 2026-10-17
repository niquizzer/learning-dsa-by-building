def sort_descending(lst:list[int]) -> list[int]:
    """ Sorts integer list descending.

    Args:
        lst(list[int]): integer list.

    Returns:
        list(int): is a new list with values
        sorted in descending order.
    """
    result = []
    dup_lst = lst
    smallest = dup_lst[0]

    if lst == []:
        return "Empty list"
    
    for item in dup_lst:
        if item.str:
            return "Cannot sort strings"
    
    for item in lst:
        for dup in dup_lst:
            if dup < item:
                smallest = dup 
        
        result.append(smallest)

    return [x for x in reversed(list(result))]