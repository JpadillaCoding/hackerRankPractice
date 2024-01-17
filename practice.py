def isSubsequence(s,t):
    # two pointer 
    # one keeps track of s, if letter is found then move s tracker
    # at end of t tracker then check if s tracker is on last position
        if len(s) == 0:
            return True
        anchor = 0
        for explorer in range(len(t)):
            if t[explorer] == s[anchor]:
                anchor += 1
            if anchor == len(s):
                return(True)
        return(False)
isSubsequence("b","abc")