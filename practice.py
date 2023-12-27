import collections

def checkInclusion(s1: str, s2: str):
    s1Chars = collections.Counter()
    windowLen = len(s1)
    # make a loop to subtract from counter all current items
    for i in range(len(s2)):
        # remove current iteration from count 
        if s2[i] in s1Chars:
            s1Chars[s2[i]] -=1
        # add previous index char back into the counter if it exist
            # check if the index is the same of moe than s1
            # check if it is in the counter 
        if i >= windowLen and s2[i-windowLen] in s1Chars:
            s1Chars[s2[i-windowLen]] += 1
            # add back into the counter

        # check if there is a match 
        if all([s1Chars[i] == 0 for i in s1Chars]):
            print(True)
    print(False)
checkInclusion("adc", "dcda")