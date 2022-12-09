import InputVars


player1 = ""
player2 =""
input2 =""

points = 0

for input in InputVars.players_input.split('\n'):
    player1 = input[0]

    input2 = input[2]

    #x =lose
    
    if input2 == "X":
        points+=0
        if player1 =="A":
            points+=3
        if player1 =="B":
            points+=1
        if player1 =="C":
            points+=2

    #y=draw
    if input2 =="Y":
        points+=3 
        if player1 =="A":
            points+=1
        if player1 =="B":
            points+=2
        if player1 =="C":
            points+=3
    
    if input2 =="Z":
        points+=6
        if player1 =="A":
            points+=2
        if player1 =="B":
            points+=3
        if player1 =="C":
            points+=1


print(points)



