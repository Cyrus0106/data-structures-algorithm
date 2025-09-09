def contains_duplicate(nums):
    # TODO
    if len(nums) != len(set(nums)): 
        return True
    else: 
        return False