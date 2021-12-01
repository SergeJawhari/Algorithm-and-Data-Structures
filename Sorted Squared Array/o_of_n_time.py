# O(n) time complexity because no sorting algorithm is being used. | O(n) space complexity because a new output array is generated and n represents the size of the array. 

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array] # initialize an array with 0's
    smallerValueIdx = 0 # set the index value of the to zero so it starts at the start of the array.
    largerValueIdx = len(array) - 1 # set the value of the index to the last number in the array so it grabs the largest value.

    # this for loop will decrement from the end of the array and place values backwards from greatest to least.
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx] # will place the pointer at the beginning of the array.
        largerValue = array[largerValueIdx] # will place the pointer at the end of the array.

        # if the absolute value of the start of the array is larger than the absolute value of the end of the array (i.e. |-7| > |6|), 
        # then the value will be squared and added to the output array; the index will then be incremented to the nextmost smallest value.
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        
        # else, the opposite will happen and the larger value will be squared and the pointer will drop to the left to the nextmost largest value.
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    # return the output array of sorted squared values.
    return sortedSquares