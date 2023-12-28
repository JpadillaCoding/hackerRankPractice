import math
def validPalindrome(s):
    # needs to read the same forward and back
    stringLen = len(s)
    # make descrpency counter
    descrepency = 0
    left = 0 
    right = len(s) -1
    # if even then add evenly both sides 
    if stringLen % 2 == 0:
        #double pointer system 
        for left in range(stringLen // 2):
            if s[left] != s[right]:
                descrepency += 1
            right -= 1
            if descrepency > 1:
                print(False)
        if descrepency <= 1:
            print(True)
        else:
            print(False)
    #else:
    # if odd then half from left and right of middle
    else: 
        for left in range(math.floor(stringLen//2)-1):
            if s[left] != s[right]:
                descrepency += 1
            right -=1
            if descrepency > 1:
                print(False)
        if descrepency <= 1:
            print(True)
        else:
            print(False)
        # if descrepency counter <= 1
            #return True
        # else False

validPalindrome('adcdcba')