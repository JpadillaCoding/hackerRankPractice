def lengthOfLongestSubstring(s):
    # make a for loop start at 0 end len of s
    # use inner loop to keep looping until a unique addition cant be made to map
    # inner loop should give a counter of how many additions can be made
    n = len(s)
    maxLength = 0
    charSet = set()
    left = 0
    
    for right in range(n):
        if s[right] not in charSet:
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
    
    return maxLength

lengthOfLongestSubstring('abcabcbb')