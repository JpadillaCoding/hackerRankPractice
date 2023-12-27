def findContentChildren(g, s):
    # already sorted? 
    # make a satisfied variable
    # start with the smallest greed (g)
        # check if the size (s) is equal or greater to g 
        # +1 to satisfied 
        # else return satisfied
    # how to traverse? 
    # outer loop looking at g 
    # inner loop looking at s and updating its position
    s.sort()
    s.sort()
    satisfied = 0 
    jStart = 0
    for i in range(len(g)):

        for j in range(jStart,len(s)):
            if s[j] >= g[i]:
                satisfied +=1
                jStart +=1
                break
            else:
                jStart += 1
    print(satisfied)

findContentChildren([1,2],[1,2,3])