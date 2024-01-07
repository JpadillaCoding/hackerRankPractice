def fib(n: int) -> int:
    nums = []
    for i in range(n+1):
    #add the current and previous to the array 
        if i == 1: 
            nums.append(1)
        elif i == 0:
            nums.append(0)
        else:
            nums.append(nums[i-1] + nums[i-2])
    print(nums[-1])
fib(3)