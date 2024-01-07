def fib(n: int) -> int:
    #base case is 0
    if n == 0: return 0 
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
fib(3)