def longestPalindrome(s):
    # loop through and make a hashmap of all the items
    odd_count = 0
    d = {}

    for ch in s:
        if ch in d:
            d[ch] += 1
        else: 
            d[ch] = 1
        if d[ch] % 2 != 0:
            odd_count += 1
        else:
            odd_count -= 1
        if odd_count > 1 :
            return len(s) - odd_count + 1
        return len(s)
    # if the amount of items in hashmap is even retunr than number, if odd then return that number
longestPalindrome("arbccccdd")
