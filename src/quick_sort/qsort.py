def qsort(arr:list[int]) -> list[int]:
    """Quicksort algorithm"""
    # Arrays w/ less than 2 elements already "sorted"
    if len(arr) < 2:
        return arr
    else:
        # Pivot of list
        pivot: int = arr[0] 

        # List partitions
        lwr_arr: list[int] = [x for x in arr[1:] if x <= pivot]
        upp_arr: list[int] = [x for x in arr[1:] if x > pivot] 

    return qsort(lwr_arr) + [pivot] + qsort(upp_arr)




        
