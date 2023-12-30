def balancedStringSplit(s):
    # loop through with a count of r and l 
    # when r.len == l.len make counter + 1
    # reset l and r count
    rCount = 0
    lCount = 0
    balanceCount = 0
    for char in range(len(s)):
        if s[char] == 'R':
            rCount +=1
        else:
            lCount +=1
        if rCount == lCount:
            balanceCount +=1
            lCount = 0
            rCount = 0
    print(balanceCount)

balancedStringSplit('LLLLRRRR')