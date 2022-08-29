def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo<=hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        if mid > 0 and mid_number < nums[mid-1]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0
