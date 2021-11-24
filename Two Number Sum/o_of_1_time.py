# O(nLog(n)) time complexity because of the sorting algorithm | O(1) space complexity because no storing structures are being utilized.

# this algorithm will use pointers initialzed at opposite points in an array (beginning and end) 
# and selectively 'close in' towards the middle to find summands for the target sum, if any.
def twoNumberSum(array, targetSum):
    # using python built in sorting function to sort an array using an optimal sorting algorithm that runs in O(n*log(n)) time.
    array.sort() 
    left = 0 # set the left pointer to the first value in the array.
    right = len(array) -1 # set the right pointer to the last value in the array.

    # this will make sure that the pointers do not overlap and repeat indexes.
    while left < right:
        currentSum = array[left] + array[right] # this will add the left pointer to the right pointer.

        # this will check if the current sum matches the target sum, if it does, then return the two values in array format.
        if currentSum == targetSum:
            return [array[left], array[right]]

        # this will check if the current sum is less than the target sum, if it is, then the left pointer 
        # will be increased, since in a sorted list, increasing the left pointer will greaten the value of the current sum.
        elif currentSum < targetSum:
            left += 1

        # this elif statement works vice versa of the above statement, instead shifting the right pointer leftward, down a sorted list to lower a value.
        elif currentSum > targetSum:
            right -= 1
    
    return [] # return an empty list if nothing is returned.