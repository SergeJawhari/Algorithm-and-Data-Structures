# O(nLog(n)) time complexity because of the sorting algorithm that is used (.sort()) | O(n) space complexity because a new output array is generated and n represents the size of the array. 

def sortedSquaredArray(array):
    squaredArray = [] # initialize a new array to store squared values in.

    # this for loop will take each value in the array and square it via ** 2, and append it to the new squared array.
    for i in array:
        squaredArray.append(i**2)
    squaredArray.sort() # sorts the squared array to make sure that the array is in ascending order.
    return squaredArray # returns the array of squared sorted values.