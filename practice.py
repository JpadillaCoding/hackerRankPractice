def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # moving it in place with appending a zero and delete in place 
        # issue of how I am to itirate?
        # make while loop- if the operation finds zero-
        # delete the zero but dont itirate forward
        # if a num is found then itierate forward
    anchor = 0
    for explorer in range(len(nums)):
        if nums[explorer] != 0:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1
moveZeroes([0,1,0,3,12])