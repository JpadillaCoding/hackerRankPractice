def findContentChildren(g, s):
    # double pointer system left is g right is s 
    # 
    g.sort()
    s.sort()

    left = 0 
    right = 0 
    counter = 0

    while left < len(g) and right < len(s):
        # while loop on left to move by one 
        if s[right] >= g[left]:
            counter += 1
            right +=1
        left += 1
    print(counter)
        

findContentChildren([1,2],[1,2,3])