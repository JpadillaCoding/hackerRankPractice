def canThreePartsEqualSum(arr):
    # get the total of the array 
    # if the total can't be divided into 3 equas parts,
    # return False since it's impossible to parition
    # get the amount needed for 1/3 of a part
    # track the amount of partitions. If 1 is found reset the partition total
    # if a second parition is found, verify the remaining amount if in fact == to avg
    total = sum(arr)
    if total % 3 != 0:
        print(False)
    avg = total // 3 
    paritionTotal = 0
    partitions = 0

    for i in range(len(arr)-1):
        paritionTotal += arr[i]
        if paritionTotal == avg:
            if partitions == 1 and sum(arr[i+1:]) == avg:
                print(True)
                break
            partitions +=1
            paritionTotal = 0
    print(False)


canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])