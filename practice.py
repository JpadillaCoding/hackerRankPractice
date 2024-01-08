def tribonacci(n: int):
    if n == 1:
        return 1
    elif n <= 0: 
        return 0 
    else:
        return (tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3))
tribonacci(4)