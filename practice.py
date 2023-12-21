from string import ascii_lowercase
def pangrams(s):
    # to lower the string
    s.lower()
    # loop through alphabet ascii
    for letter in ascii_lowercase:
    # check if the letter is in string
        if letter not in s:
    # if not return "not pangram"
            return ("not pangram")
    # end of loop reuturn "pangram"
    return ("pangram")

pangrams("The quick brown fox jumps over the lazy do")