def twoSum(numbers,target):
    # find if the target can be found with two nums in array
    # itirate through array, and subtract what we're looking for from current i
    # if that num is contaiend in the array continue to find index
    # else continue to next itiration

    for i in range(len(numbers)):
        findNum = target - numbers[i]
        if findNum in numbers:
            for j in range(i+1,len(numbers)):
                if numbers[j] == findNum:
                    print([i+1,j+1])

twoSum([-1,0], -1)