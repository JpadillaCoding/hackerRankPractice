def longestPalindrome(s):
    # loop through and make a hashmap of all the items
    items = {}
    evenCount = 0
    for i in range(len(s)):
        items[s[i]] = 1 + items.get(s[i],0)
        # if item i not contained then init it
        if items[s[i]] % 2 == 0:
            evenCount +=1
    # check hashmap for number of even numbers
    if evenCount > 0:
        if evenCount < len(s):
            print(evenCount + 1)
        else: 
            print(evenCount)
    else: 
        print(0)
        
    # if the amount of items in hashmap is even retunr than number, if odd then return that number
longestPalindrome("abccccdd")
