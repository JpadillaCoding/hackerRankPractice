def checkInclusion(s1: str, s2: str):
    # make a window the size of s1
    # slide one by one and check window if it contains all the letters
        # make a dict with all the letters in the current window and amount
        # compare each iteration between the window and s1
    childStringLen = len(s1)
    ParentStringLen = len(s2)
    childCharCount = {}
    parentCharCount = {}

    #make edge case in case s1 is longer than s2 to return false
    if childStringLen > ParentStringLen:
        print(False)
    for char in range(childStringLen):
        if s1[char] in childCharCount:
            childCharCount[s1[char]] += 1
        else:
            childCharCount[s1[char]] = 1
    
    for char in range(childStringLen):
        # establish the first childStringLen amount of charc in s2
        if s2[char] in parentCharCount:
            parentCharCount[s2[char]] += 1
        else:
            parentCharCount[s2[char]] = 1
    # now check the initial sets
    if childCharCount == parentCharCount:
        print(True)

    # now loop through and add the current itieration of s2
    for char in range(childStringLen,ParentStringLen):
        if s2[char] in parentCharCount:
            parentCharCount[s2[char]] += 1
        else:
            parentCharCount[s2[char]] = 1
    # remove the left pointer from the parent dict 
        parentCharCount[s2[char-childStringLen]] -= 1
        if parentCharCount[s2[char-childStringLen]] == 0:
            parentCharCount.pop(s2[char-childStringLen])
    # if the left pointers char ==0 then remove the letter from dict
    # now compare the 2 dicts
        if (childCharCount == parentCharCount):
            print(True)
        # if they match return true 
    # keep looping, end of loop return false
    print(False)
    # edge case for len of 1 on s2 and s1?
checkInclusion("adc", "dcda")