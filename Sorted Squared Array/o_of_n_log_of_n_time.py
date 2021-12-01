# O(nLog(n)) time complexity because of the sorting algorithm that is used (.sort()) | O(n) space complexity because a new output array is generated and n represents the size of the array. 

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array] # initialize an empty array with 0's 

    # this for loop will get the value of the array at each index placement and square it, adding it to the new array.
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    # sort the array to ensure that it is in ascending order.
    sortedSquares.sort()

    # return the output array.
    return sortedSquares