import random
midwestTeams = [["Kansas",1], ["Texas", 6]]
#eastTeams = [["Bay",1], ["Norfolk",16], ["UNC", 8], ["MARQ", 9], ["STMary", 5], ["WYO/IU", 12], ["UCLA", 4], ["Akron", 13], ["Texas", 6], ["VT", 11], ["Pur", 3], ["Yale", 14], ["MURR", 7], ["SF", 10], ["UK", 2], ["STPETE", 15]]
#westTeams = [["Gonzaga",1], ["GA ST",16], ["Boise", 8], ["Mem", 9], ["UConn", 5], ["NMSU", 12], ["Ark", 4], ["Vermont", 13], ["Bama", 6], ["Rutgers/Notre Dame", 11], ["TTU", 3], ["MON ST", 14], ["MSU", 7], ["DAVID", 10], ["DUKE", 2], ["CS FUL", 15]]

team1 = 0
team2 = 1

teamrank1 = midwestTeams[team1][1]
teamrank2 = midwestTeams[team2][1]

while team2 <=3:
    total = teamrank1 + teamrank2
    #print(total)
    pick = random.randint(0, total)
    #print(pick)
    if pick > teamrank1:
        winner = midwestTeams[team1][0]
    else:
        winner = midwestTeams[team2][0]
    print("The Winner is", winner)
    team1 += 2
    team2 += 2