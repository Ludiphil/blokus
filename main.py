import os

from Piece import Piece
from Player import Player
import random
from tkinter import *

#mat=[[0 for j in range(22)] for i in range(22)]

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

    listOfPieces = []
    listOfPieces.append(p1)
    listOfPieces.append(p2)
    listOfPieces.append(p3)
    listOfPieces.append(p4)
    listOfPieces.append(p5)
    listOfPieces.append(p6)
    listOfPieces.append(p7)
    listOfPieces.append(p8)
    listOfPieces.append(p9)
    listOfPieces.append(p10)
    listOfPieces.append(p11)
    listOfPieces.append(p12)
    listOfPieces.append(p13)
    listOfPieces.append(p14)
    listOfPieces.append(p15)
    listOfPieces.append(p16)
    listOfPieces.append(p17)
    listOfPieces.append(p18)
    listOfPieces.append(p19)
    listOfPieces.append(p20)
    listOfPieces.append(p21)
    return listOfPieces

def colorAsssignment():
    colors = ["blue", "green", "red", "yellow"]

    randomColor1 = random.choice(colors)
    colors.remove(randomColor1)

    randomColor2 = random.choice(colors)
    colors.remove(randomColor2)

    randomColor3 = random.choice(colors)
    colors.remove(randomColor3)

    randomColor4 = colors[0]
    listColor = []
    listColor.append(randomColor1)
    listColor.append(randomColor2)
    listColor.append(randomColor3)
    listColor.append(randomColor4)
    return listColor

def colorSwitch(color):
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
    player1 = Player(colorOrder[0],listOfFullPieces,"Jacky")
    player2 = Player(colorOrder[1],listOfFullPieces,"Jocelyn")
    player3 = Player(colorOrder[2],listOfFullPieces,"Brice")
    player4 = Player(colorOrder[3],listOfFullPieces,"Oui")

    listOfPlayers = {player1,player2,player3,player4}

    for p in listOfPlayers:
        print(p.listPieces[17].mat)
    for p in listOfPlayers:
        print(p.color)

    for p in listOfPlayers:
        p.color = colorSwitch(str(p.color))

    for p in listOfPlayers:
        print(p.color)


preparationStart()

#
# mat=[[1 for j in range(22)] for i in range(2)]
# mat+=[[0 for j in range(22)] for i in range(18)]
# mat+=[[1 for j in range(22)] for i in range(2)]
#
#
#
#
# # for line in mat:
# #     print (line)
# print("----------------------------------------------------------")
# for row in mat:
#     for i,col in enumerate(row):
#         if i == 0 or i == 1 or i == 20 or i == 21:
#             row[i]=1
#
# # for line in mat:
# #     print (line)



mat = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]for i in range(18)]

mat.insert(0, [1 for j in range(22) for i in range(1)])
mat.insert(1, [1 for j in range(22) for i in range(1)])
mat.append([1 for j in range(22) for i in range(1)])
mat.append([1 for j in range(22) for i in range(1)])

for line in mat:
    print(line)

i = 22
for x in range(len(mat)):
    for y in range(i):
        print(x , y)

i0 = 1


#i1 = Tk.PhotoImage(file="Z:\Projet_B\Carré_Blanc.png")



root = Tk()
cnv=Canvas(root, width=800, height=800, bg="white")
cnv.pack(padx=200, pady=200)

here = os.getcwd()
uriCB = os.path.join(here, "Carré_Blanc.png")
uriCN = os.path.join(here, "Carré_Blanc.png")

print(uriCB)


# Création de l'objet PhotoImage :
if i0 == 0:
    i0 = PhotoImage(file=uriCB)
if i0 == 1:
    i0 = PhotoImage(file=uriCN)

# Affichage de l'image :
Image_Affichee = cnv.create_image(0, 100, image = i0, anchor='nw')
Image_Affichee = cnv.create_image(0, 100, image = i0, anchor='nw')


root.mainloop()