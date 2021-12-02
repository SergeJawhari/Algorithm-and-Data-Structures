# My take on this problem
# Author: Sirage El-Jawhari

# O(n) time complexity where n is the length of the array | O(n) space complexity because the dictionary must be added to and updated.

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0,0,1]

def tournamentWinner(competitions, results):

    resultsIndex = 0

    winnersPoints = {}

    for i in results:
        if i == 0:
            if (competitions[resultsIndex][1]) in winnersPoints:
                winnersPoints[(competitions[resultsIndex][1])] += 3
            else:
                winnersPoints[(competitions[resultsIndex][1])] = 3

            if (competitions[resultsIndex][0]) not in winnersPoints:
                winnersPoints[(competitions[resultsIndex][0])] = 0

        elif i == 1:
            if (competitions[resultsIndex][0]) in winnersPoints:
                winnersPoints[(competitions[resultsIndex][0])] += 3
            else:
                winnersPoints[(competitions[resultsIndex][0])] = 3

            if (competitions[resultsIndex][1]) not in winnersPoints:
                winnersPoints[(competitions[resultsIndex][1])] = 0
        
        resultsIndex += 1
    
    winner = max(winnersPoints, key = winnersPoints.get)
    
    return winner


tournamentWinner(competitions, results)
