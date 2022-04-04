def minSubArrayLen(target: int, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    
    #We're going to use a sliding window approach to this problem
    
    #Our left pointer
    left = 0
    
    #length of the current smallest subarray greater than or equal to target
    length = float("inf")
    
    #A a rolling sum of nums
    total = 0
    
    #Iterating through the nums array, we have our right pointer
    for right in range(len(nums)):
        
        #We add to total
        total += nums[right]
        
        #While total >= target check the length, and append the total and left pointers
        while total >= target:
            
            total -= nums[left]
            length = min(length, right - left + 1)
            left += 1
            
    #If the length is infinity than that means we never found a value greater than or equal to the target. return 0        
    if length == float("inf"):
        return 0
    
    #Just return the length
    return length

numeros = [1,4,4]

print(minSubArrayLen(4, numeros))