# O(n) time complexity for using a HashTable, which operates in constant time | O(n) space complexity because values are being stored in a HashTable.

def twoNumberSum(array, targetSum):
    numbers = {} # initializes an empty dictionary.
    for number in array: # this will go through all values in the array and can be referenced by the 'number' variable.

        # if the target sum minus the number in the array exists in the dictionary of numbers, 
        # then the summand is found and the formula of: summand1 + summand2 = targetSum falls true and can be returned.
        # else, the dictionary will be updated with the new number and a True denoting that the value already exists in the table.
        if targetSum - number in numbers:  
            return [targetSum - number, number]
        else:
            numbers[number] = True
    
    # return an empty list if nothing is returned.
    return []