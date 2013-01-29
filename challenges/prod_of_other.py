from operator import mul

def make_prod_ls(ls, zero_count, zero_index, prod_of_nums):
    if zero_count >= 1:
        # more than 1 zero: prod_ls contains all 0's
        prod_ls = [0] * len(ls)
        if zero_count == 1:
        # 1 zero: set element in prod_ls at zero_index to prod_of_nums
            prod_ls[zero_index]=prod_of_nums 
    else:
        prod_ls = [prod_of_nums/n for n in ls] 
    return prod_ls

# ls is a list of integers
def prod_of_other_nums(ls):
    prod_ls = []
    if len(ls) == 1:     # returns empty list if length of ls is 1
        return prod_ls
    
    zero_count, zero_index =0, 0
    prod_of_nums = 1 

    for i in range(len(ls)):    # what is run-time for len(ls)
        if ls[i] == 0:
            zero_index = i
            zero_count += 1
        else:
            prod_of_nums *= ls[i] # product of all nums (except 0) in ls
    prod_ls = make_prod_ls(ls, zero_count, zero_index, prod_of_nums)
    return prod_ls

# not used
def get_prod(ls):
    "calculate the product of all nums, excluding 0, in list"
    return reduce(mul, [x for x in ls if x !=0])

