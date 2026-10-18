from typing import Any

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

def calculate_factorial(num:int) -> int:
    """
    Base Case:
        num(int): is zero

    Recursive Case:
        num(int): not zero
    """
    if num == 1:
        return 1
    else:
        return num * calculate_factorial(num - 1)
    
def recursive_sum(lst:list[int]) -> int:
    if lst == []:
        return 0
    else:
        first_num = lst.pop(0)
        print(first_num, " + ", lst)
        return first_num + recursive_sum(lst) 

def count_list_items(lst:list[Any]) -> int:
    """
    Base Case:
        Empty list

    Recursive Case:
        Function pops item from list and 
        calls itself
    """
    if lst == []:
        return 0
    else:
        lst.pop(0)
        return 1 + count_list_items(lst)

    

    
    


