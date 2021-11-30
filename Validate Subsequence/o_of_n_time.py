# O(n) time because it runs in dependency of the length of the main array (named: array) | O(1) space because nothing additional is being stored.

def isValidSubsequence(array, sequence):
    arrayIndex = 0 # initialize the index of the array at 0 so the pointer begins at the start of the array.
    sequenceIndex = 0 # initialize the index of the sequence at 0 so the pointer begins at the start of the sequence.

    # will continue while the indexes are within bounds of both the sequence and array lengths.
    while arrayIndex < len(array) and sequenceIndex < len(sequence):

        # if the value of the array is equal to the value of the sequence, the sequence index will be increases to point to the next value in the list.
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1

        # continue to iterate through the array even if sequence is not found, to check sequence value with the next array value until the end of the array list is reached.
        arrayIndex += 1

    # returns a boolean value on whether the sequence index has reached the end of the list; if it has the same value as the length,
    # then the algorithm is successful because all sequence values were equal to all array values, in order, and will return true.
    return sequenceIndex == len(sequence)