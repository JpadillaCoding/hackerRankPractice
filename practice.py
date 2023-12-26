def characterReplacement(s,k):
    # make a max count starting at 0 
    # keep track of the most popular letter
    # the window permits only 2 deviations from popular letter 
      # possibly do this by removing 2 from window and comparing from most popular
    # keep updating max as long as that condition is met  
    # if not met then move window over by 1 
    # AABABBA
    # start k + i 
    # check for most popular 
    # AA most popular A max of 2
    # increase window 
    # AAB stil valid because lenght- k = most popular max of 3
    # AABA still valid because length - k = most popular max of 4 
    # AABAB not valid because length - k > most popular max of 4 
    # slide window over ABAB maintain the max window size. invalid because max is 2.
    # slide window over BABB. valid because most popular letter length - k = most popular letter 4
    # BABBA invalid bc length - k > most popular letter 

    maxCount = 0
    left = 0 
    arrLen = len(s)
    characters = {}
    for right in range(arrLen):
        if s[right] not in characters:
            characters[s[right]] = 1
        else:
            characters[s[right]] += 1
        window = right - left + 1
        #get window
        # compare most popular + k 
        if max(characters.values()) + k >= window:
            maxCount = max(maxCount, window)
        # if equal or more than my window size, make the max count this current amount
        else: 
            characters[s[left]] -= 1
            left += 1
        # if less than window size, move left by one and update my charc count
    print(maxCount)

characterReplacement('ABAB', 2)