def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # moving it in place with appending a zero and delete in place 
        # issue of how I am to itirate?
        # make while loop- if the operation finds zero-
        # delete the zero but dont itirate forward
        # if a num is found then itierate forward
    i = 0
    length = len(nums)
    while i < length - 1:
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            length -= 1
        else:
            i += 1
    print(nums)
moveZeroes([0,1,0,3,12])