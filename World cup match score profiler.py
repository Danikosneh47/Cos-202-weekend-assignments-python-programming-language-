print ( "World cup match score profiler")
team1 = input("Enter Home Team Name: ")
score1 = int(input(f"Enter {team1} score: "))
team2 = input("Enter Away Team Name: ")
score2 = int(input(f"Enter {team2} score: "))

diff = abs(score1 - score2)

if score1 == score2:
    print("Result: Stalemate Draw")
else:
    
    if diff == 1:
        classification = "Narrow Victory"
    elif 2 <= diff <= 3:
        classification = "Heavy Victory"
    else:
        classification = "Thrashing"
        
    winner = team1 if score1 > score2 else team2
    print(f"Result: {winner} won! Match Classified as a: {classification}")
