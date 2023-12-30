def maximumTime(time: str) -> str:
    # there are maximum digits per slot 
    # remove the semicolon
    # loop through and check for question mark
    # make if statments for max of that spot
    # make the maximum of that current spot
    # join together with smicolon
    nums = list(time)
# hour one being a 2 depends on:
    # [1] being [0] or [?]
    if nums[0] == '?':
        if  nums[1] =='?' or int(nums[1]) < 4:
            nums[0] = '2'
        else:
            nums[0] = '1'
    if nums[1] == '?':
        if nums[0] == '2':
            nums[1] = '3'
        else:
            nums[1] = '9'
    if nums[3] == '?':
        nums[3] = '5'
    if nums[4] == '?':
        nums[4] = '9'

    print(''.join(nums))

maximumTime('?5:03')