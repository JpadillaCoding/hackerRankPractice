import re
def isPalindrome(s):
    # lowercase all chars
    # trim all non letters and nums

    trimmedString = re.sub('[\W_]+', '', s).lower()
    left = 0
    right = len(trimmedString)-1

    while left < right:
        if trimmedString[left] == trimmedString[right]:
            left += 1
            right -= 1
        else:
            print(False)
    print(True)

isPalindrome(" ")