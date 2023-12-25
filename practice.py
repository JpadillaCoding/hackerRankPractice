def lengthOfLongestSubstring(s):
    # make a for loop start at 0 end len
    # use inner loop to keep looping until a unique addition cant be made to map
    # inner loop should give a counter of how many additions can be made
    maxCount = 0
    for i in range(len(s)):
        counter = 0
        uniqueChar = {}
        for j in range(i,len(s)):
            if s[j] not in uniqueChar:
                counter += 1
                # add to the dict
                uniqueChar[s[j]] = 0
            else: 
                # break out of current inner loop
                break
        if counter > maxCount:
            maxCount = counter
    print(maxCount)
    # for effeciency add a check if the remainder is shorter than the maxcount
    # end early in outer loop

lengthOfLongestSubstring('pwwkew')