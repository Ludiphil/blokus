from Piece import Piece
from Player import Player
import random

mat=[[0 for j in range(22)] for i in range(22)]

def affichepiece(quetru):
    for line in quetru.mat:
        print(line)


def creationPieces():
    p1 = Piece(1, [1])
    p2 = Piece(2, [[1], [1]])
    p3 = Piece(3, [[1], [1], [1]])
    p4 = Piece(3, [[1, 0], [1, 1]])
    p5 = Piece(4, [[1], [1], [1], [1]])
    p6 = Piece(4, [[0, 1], [0, 1], [1, 1]])
    p7 = Piece(4, [[1, 0], [1, 1], [1, 0]])
    p8 = Piece(4, [[1, 1], [1, 1]])
    p9 = Piece(4, [[1, 1, 0], [0, 1, 1]])
    p10 = Piece(5, [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]])
    p11 = Piece(5, [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]])
    p12 = Piece(5, [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]])
    p13 = Piece(5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]])
    p14 = Piece(5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]])
    p15 = Piece(5, [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]])
    p16 = Piece(5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]])
    p17 = Piece(5, [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    p18 = Piece(5, [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    p19 = Piece(5, [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    p20 = Piece(5, [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    p21 = Piece(5, [[0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    return {p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21}

def colorAsssignment():
    colors = ["blue", "green", "red", "yellow"]

    randomColor1 = random.choice(colors)
    colors.remove(randomColor1)

    randomColor2 = random.choice(colors)
    colors.remove(randomColor2)

    randomColor3 = random.choice(colors)
    colors.remove(randomColor3)

    randomColor4 = colors[0]
    return {randomColor1,randomColor2,randomColor3,randomColor4}

def colorOrder(color):
    switch={
       'blue': 1,
       'yellow': 2,
       'red': 3,
       'green': 4,
       }
    return switch.get(color,'Color is not in list')

def preparationStart():
    listOfFullPieces=creationPieces()

    colorOrder = colorAsssignment()
    player1 = Player(list(colorOrder)[0],listOfFullPieces,"Jacky")
    player2 = Player(list(colorOrder)[1],listOfFullPieces,"Jocelyn")
    player3 = Player(list(colorOrder)[2],listOfFullPieces,"Brice")
    player4 = Player(list(colorOrder)[3],listOfFullPieces,"Oui")

    listOfPlayers = {player1,player2,player3,player4}

    for p in listOfPlayers:
        print(p.color)

    for p in listOfPlayers:
        p.color = colorOrder(p.color)

    for p in listOfPlayers:
        print(p.color)


preparationStart()


mat=[[1 for j in range(22)] for i in range(2)]
mat+=[[0 for j in range(22)] for i in range(18)]
mat+=[[1 for j in range(22)] for i in range(2)]




# for line in mat:
#     print (line)
print("----------------------------------------------------------")
for row in mat:
    for i,col in enumerate(row):
        if i == 0 or i == 1 or i == 20 or i == 21:
            row[i]=1

# for line in mat:
#     print (line)