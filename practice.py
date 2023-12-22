def findAnagrams(s, p):
    positionArg=[]
    hashP = {}
    hashS ={}
    if(len(s) < len(p)):
        return positionArg
    
    for i in range(len(p)):
        if p[i] in hashP:
            hashP[p[i]] = hashP[p[i]] + 1
        else:
            hashP[p[i]] = 1

    for i in range(len(p)):
        if s[i] in hashS:
            hashS[s[i]] = hashS[s[i]] + 1
        else:
            hashS[s[i]] = 1
    if hashS == hashP: positionArg.append(0)


    leftPoint = 0 
    for rightPoint in range(len(p),len(s)):
        hashS[s[rightPoint]] = 1 + hashS.get(s[rightPoint],0)
        hashS[s[leftPoint]] -= 1 

        if hashS[s[leftPoint]] == 0:
            hashS.pop(s[leftPoint])
        leftPoint +=1

        if hashS == hashP: positionArg.append(leftPoint)
    return positionArg





findAnagrams("cbaebabacd","abc")
