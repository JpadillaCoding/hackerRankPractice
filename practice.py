
def nextGreatestLetter(letters, target):
    for i in range(len(letters)):
        # if on last position then return letters[0]
        if letters[i] == target:
            if i == len(letters)-1:
                print(letters[0])
            else:
                print(letters[i + 1])
        if ord(letters[i]) > ord(target):
            print(letters[i])
    # find the first letter that is after the target else letters[0]
    print(letters[0])
    # use binary search to find optimal
nextGreatestLetter(["x","x","y","z"], 'z')