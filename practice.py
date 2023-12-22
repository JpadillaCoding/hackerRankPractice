def longestPalindrome(s):
    # loop through and make a hashmap of all the items
    items = {}
    evenCount = 0
    if len(s) == 1 or len(s) == 2:
        return 1

    for i in range(len(s)):
        items[s[i]] = 1 + items.get(s[i],0)
        # if item i not contained then init it
        if items[s[i]] % 2 == 0:
            evenCount +=1
    # check hashmap for number of even numbers
    evenCount = evenCount * 2
    if evenCount > 0:
        if evenCount < len(s):
            return (evenCount + 1)
        else: 
            return (evenCount)
    else: 
        return (0)
        
    # if the amount of items in hashmap is even retunr than number, if odd then return that number
longestPalindrome("abccccdd")
