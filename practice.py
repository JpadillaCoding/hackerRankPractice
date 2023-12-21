from string import ascii_lowercase
def pangrams(s):

    lowered = s.lower()
    for letter in ascii_lowercase:
        if letter not in lowered:
            print ("not pangram")
    print ("pangram")

pangrams("We promptly judged antique ivory buckles for the next prize")