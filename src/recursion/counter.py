def recursion_counter() -> list[int]:
    """
    Base Case:
        Counter equals zero.

    Recursive Case:
        Counter is not zero
    """
    counter = 3
    result = []

    while counter != 0:
        result.append(counter)
        counter -= 1
    
    return result

