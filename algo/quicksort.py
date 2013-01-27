import random

def quicksort(ls):
    if ls == []:
        return ls
    else:
        pivot = random.randrange(0,len(ls))
        pivot = ls.pop(pivot)
        left = [x for x in ls if x < pivot]
        right = [x for x in ls if x >= pivot]
        sorted_left = quicksort(left)
        sorted_right = quicksort(right) 
        return sorted_left + [pivot] + sorted_right 
