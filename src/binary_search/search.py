def binary_search(path:str, target:str) -> int:
    """Conducts binary search on text files to find target id.
    
    Args:
        path(str): is the filepath to text file.
        target(str): is the target value in text file.
        
    Returns:
        int: returns the target id as an int.
        
    Raises:
        -99: is an empty list
        -1: means the target cannot be found in list"""

    try:
        # loads text file
        with open(path, 'r') as f:
            lst = []
            first_line = f.readline().strip()
            if first_line == "":
                return -99

            # Storing text lines in list
            for line in f:
                line = line.strip()
                lst.append(int(line))
            
            lst.sort()
    except:
        return -99
    
    # Binary search
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2

        if lst[mid] == target:
            return lst[mid]

        elif lst[mid] > target:
            last = mid - 1

        elif lst[mid] < target:
            first = mid + 1

    return -1


def linear_search(path:str, target:str) -> int:
    """Conducts linear search on text files to find target id.
    
    Args:
        path(str): is the filepath to text file.
        target(str): is the target value in text file.
        
    Returns:
        int: returns the target id as an int.

    Returns:
        int: returns the target id as an int."""

    # Loads text file
    with open(path, 'r') as f:
        target = str(target)
        first_line = f.readline().strip()
        if first_line == "":
            return -99

        for line in f:
            line = line.strip()

            if line == target:
                return int(line)
    return -1
