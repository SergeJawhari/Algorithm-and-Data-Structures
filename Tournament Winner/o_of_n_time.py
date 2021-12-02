# O(n) time complexity where n is the number of competitions | O(k) space complexity where k is the number of keys (teams) competing in the competition.

HOME_TEAM_WON = 1 # create a static variable that denotes if the home team has won a competition.

def tournamentWinner(competitions, results):
    currentBestTeam = "" # this will initialize the best team to an empty string.
    scores = {currentBestTeam: 0} # this initializes a dictionary with the empty string and a value of 0.

    # this for loop will give the index value and each competition for the set of competitions.
    for idx, competition in enumerate(competitions):
        result = results[idx] # this will get the result at the current index location.
        homeTeam, awayTeam = competition # this will decompose each competition into two separate teams.

        # this statement will set the winning team equal to the home team if the home team has won the game, i.e. the home team wins if the results are: 1 in the array.
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam 

        # this is a function that will update the scores of the teams, passing 3 points if the team has won.
        updateScores(winningTeam, 3, scores)

        # this statement sets the current best team to the team that has the most points and checks it against the team that has just won a competition.
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam # returns the current best team.

def updateScores(team, points, scores):

    # if the team is currently not in the dictionary, then the dictionary will be updated with that team along with a score of 0 to initialize.
    # else, it will go on to the next clause and the points will be updated. 
    if team not in scores:
        scores[team] = 0

    # since the winning team is passed into this function, the points (3 in this case) will be added to the teams current score, updating it.
    scores[team] += points