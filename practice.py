
def nextGreatestLetter(letters, target):
    length = len(letters)
    pointer = length - 1
    while pointer >= 0:
        # check if its less than target and not -1
        if (target == letters[pointer] or ord(target) > ord(letters[pointer])) and pointer == length-1:
            print(letters[0])
        elif target == letters[pointer] or ord(target) > ord(letters[pointer]):
            print(letters[pointer + 1])
        # check if less than target 
        pointer -=1
    print(letters[0])
nextGreatestLetter(["c","f","j"], 'c')