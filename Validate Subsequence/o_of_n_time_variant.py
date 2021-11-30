# O(n) time because it runs in dependency of the length of the main array (named: array) | O(1) space because nothing additional is being stored.

def isValidSubsequence(array, sequence):
    sequenceIndex = 0 # initialize the index of the sequence at 0 so the pointer begins at the start of the sequence.

    # this for loop will iterate through all the values in the array.
    for value in array:

        # if the sequence index is equal to the length of the sequence, then we have reached the end of the sequence check and thusly a success.
        if sequenceIndex == len(sequence):
            break
        # if the sequence value is equal to the array value, then the sequence index is incremented.
        # note: the array is automatically iterated via the for loop.
        if sequence[sequenceIndex] == value:
            sequenceIndex += 1
    
    # returns a boolean value on whether the sequence index has reached the end of the list; if it has the same value as the length,
    # then the algorithm is successful because all sequence values were equal to all array values, in order, and will return true.
    return sequenceIndex == len(sequence)