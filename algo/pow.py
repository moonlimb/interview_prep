import timeit

"recursive solution; O(n)"
def pow_recur(x,n):
    return x*pow(x,n-1)

def square(x):
    return x*x

"O(log n)"
def pow(x,n):    
    if n == 0:
        return 1
    if n%2 == 0: #n is even
        return square(pow(x,n/2))
    else:
        return x*pow(x,n-1)
