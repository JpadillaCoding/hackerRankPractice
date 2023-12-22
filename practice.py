def countGoodSubstrings(s):
    # make siding door with size of 3 
    # each addition check if the letter is contained
    # if letter is contained then continue
    # letter not contaiend add to counter
    counter = 0
    if len(s) < 3: 
        return counter
    for i in range(len(s)-2):
        if(s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]):
            counter+=1
    return(counter)
countGoodSubstrings("aababcabc")

















"""     arrayLength = len(nums)
    if arrayLength < k:
        print(0)
    for i in range(arrayLength):
        subArr = nums[i:i+k]
        if len(subArr) == 4: print(subArr) """