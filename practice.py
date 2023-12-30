def maximum69Number (num):
    # loop through and swap first 6 I come across.
    # keep track of the last 9 index
    # if no 6 was flipped then flip the 9 
    arg = list(str(num))
    for number in range(len(arg)):
        if arg[number] == '6':
            arg[number] = '9'
            print(int(''.join(arg)))
    print(int(''.join(arg)))


maximum69Number(9999)