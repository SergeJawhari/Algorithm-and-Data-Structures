# My take on this problem
# Author: Sirage El-Jawhari

# O(n^2) time complexity where n is the length of the array and the maximum value must be found at the end, which is another loop | O(k) space complexity where k is the number of keys (teams) competing in the competition.

def tournamentWinner(competitions, results):

    resultsIndex = 0 # initialized the index of the results to 0.

    winnersPoints = {} # created an empty dictionary.

    for result in results:

        # this if statement will check if the value of each result to see if it is the away team that has won.
        if result == 0:

            # if the key or name of team has won, then the key value will be updated with a +3 points for winning.
            if (competitions[resultsIndex][1]) in winnersPoints:
                winnersPoints[(competitions[resultsIndex][1])] += 3

            # else, the key value pair will be initialized with a win, denoted by the 3 initial points for winning.
            else:
                winnersPoints[(competitions[resultsIndex][1])] = 3

            # if the losing team is not in the dictionary, then it will be added with the 0 points for losing.
            if (competitions[resultsIndex][0]) not in winnersPoints:
                winnersPoints[(competitions[resultsIndex][0])] = 0

        # this statement works in vice verse of the if statement above, instead checking if the home team has won.
        elif result == 1:
            if (competitions[resultsIndex][0]) in winnersPoints:
                winnersPoints[(competitions[resultsIndex][0])] += 3
            else:
                winnersPoints[(competitions[resultsIndex][0])] = 3

            if (competitions[resultsIndex][1]) not in winnersPoints:
                winnersPoints[(competitions[resultsIndex][1])] = 0
        
        resultsIndex += 1 # this will increment the result index by 1 point.
    
    winner = max(winnersPoints, key = winnersPoints.get) # the winner of the competition will be the key of the value that has the greatest number value.
    
    return winner # the string key value will be returned.