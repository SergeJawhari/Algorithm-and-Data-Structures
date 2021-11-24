# O(n^2) time complexity because of double for loops | O(1) space complexity because there are no storage structures used (HashTables)

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1): # iterates through array before last value.
        firstNum = array[i] # initializes firstNum variable with the value of the i index value.
        for j in range(i + 1, len(array)): # iterates through the rest of the numbers in the array.
            secondNum = array[j] # j will iterate all the way to the end of the array.
            if firstNum + secondNum == targetSum: # if case to check if the first number and second number equal the target sum.
                return [firstNum, secondNum] # will return the two values in an array format if the case is found to be true.
    return [] # else case will return an empty array denoting that the target sum cannot be calculated.