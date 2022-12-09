import copy
import os

import cnv as cnv

from Piece import Piece
from Player import Player
import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk

from PIL import ImageTk, Image
import numpy as np

def rotate(piece):


    if piece.nbTour != 7:
        if (piece.nbTour == 3):
            piece.mat = np.transpose(piece.mat)

        else:
            piece.mat = np.rot90(piece.mat)

        piece.nbTour += 1
    else:
        piece.mat = np.transpose(piece.mat)
        piece.nbTour = 0


def creationPieces(color):
    here = os.getcwd()
    # print(here)

    temp = 1
    listP1 = []
    listP1.append(temp)

    url = os.path.join(here + "\images\\" + "1" + "_" + color + ".png")
    p1 = Piece(1,1, [listP1], -1, url)
    url = os.path.join(here + "\images\\" + "2" + "_" + color + ".png")
    p2 = Piece(2,2, [[1, 0], [1, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "3" + "_" + color + ".png")
    p3 = Piece(3,3, [[1, 0, 0], [1, 0, 0], [1, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "4" + "_" + color + ".png")
    p4 = Piece(4,3, [[1, 0, 0], [1, 1, 0], [0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "5" + "_" + color + ".png")
    p5 = Piece(5,4, [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "6" + "_" + color + ".png")
    p6 = Piece(6,4, [[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "7" + "_" + color + ".png")
    p7 = Piece(7,4, [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "8" + "_" + color + ".png")
    p8 = Piece(8,4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "9" + "_" + color + ".png")
    p9 = Piece(9,4, [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "10" + "_" + color + ".png")
    p10 = Piece(10,5, [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "11" + "_" + color + ".png")
    p11 = Piece(11,5, [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "12" + "_" + color + ".png")
    p12 = Piece(12,5, [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "13" + "_" + color + ".png")
    p13 = Piece(13,5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "14" + "_" + color + ".png")
    p14 = Piece(14,5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "15" + "_" + color + ".png")
    p15 = Piece(15,5, [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "16" + "_" + color + ".png")
    p16 = Piece(16,5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "17" + "_" + color + ".png")
    p17 = Piece(17,5, [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "18" + "_" + color + ".png")
    p18 = Piece(18,5, [[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "19" + "_" + color + ".png")
    p19 = Piece(19,5, [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "20" + "_" + color + ".png")
    p20 = Piece(20,5, [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)
    url = os.path.join(here + "\images\\" + "21" + "_" + color + ".png")
    p21 = Piece(21,5, [[0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], -1, url)


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
    colors = ["bleu", "vert", "rouge", "jaune"]

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
       'bleu': 1,
       'jaune': 2,
       'rouge': 3,
       'vert': 4,
       }
    return switch.get(color,'Color is not in list')

def preparationStart():


    colorOrder = colorAsssignment()

    player1 = Player(colorSwitch(colorOrder[0]),creationPieces(colorOrder[0]), "Joueur 1")
    player2 = Player(colorSwitch(colorOrder[1]),creationPieces(colorOrder[1]), "Joueur 2")
    player3 = Player(colorSwitch(colorOrder[2]),creationPieces(colorOrder[2]), "Joueur 3")
    player4 = Player(colorSwitch(colorOrder[3]),creationPieces(colorOrder[3]), "Joueur 4")

    listOfPlayers = [player1, player2, player3, player4]

    # for player in listOfPlayers:
    #     for p in player.listPieces:
    #         print(p.url)

    return listOfPlayers


listOfPlayers = preparationStart()


mat=[[1 for j in range(22)] for i in range(2)]
mat+=[[0 for j in range(22)] for i in range(18)]
mat+=[[1 for j in range(22)] for i in range(2)]



mat = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]for i in range(20)]


def displayMat(mat):
    print("-------------------------------------------------------------------------")
    for line in mat:
        print(line)
    print("-------------------------------------------------------------------------")
def displayMatListed(mat):
    print("-------------------------------------------------------------------------")
    for e in mat:
        for line in e:
            print(line)
    print("-------------------------------------------------------------------------")


def displayOrder(listOfPlayers):
    print("voici l'ordre des joueurs : \n")

    for pl in listOfPlayers:

        print(pl.name + " n°" + str(pl.color))

isEnd = False
isEndTurn = False

def displayListPieces(listOfPieces):
    for p in listOfPieces:
        print("Pièce " + str(p.id) + " :")
        for line in p.mat:
            print(line)

def replacePiecesWithGoodNumbers(listOfPlayers):
    for p in listOfPlayers:
        for pi in p.listPieces:
            for line in pi.mat:
                for i in range (len(line)):
                    if line[i] == 1:
                        line[i] = p.color



def placePiece(piece, mat, coords, player):
    temp = coords[0] + coords[1]
    y = int(temp)
    temp = coords[2] + coords[3]
    x = int(temp)
    rx = 0
    ry = 0
    tx = 0
    ty = 0
    for line in piece.mat:
        for n in range(len(line)):
            if line[n] == player.color:

                rx = x + int(tx)
                ry = y + int(ty)

                print(rx, 'y :', ry)
                mat[rx][ry] = player.color
            ty += 1
        ty = 0
        tx += 1


    return mat


def checkPieceInCorner(mat, player):
    isInCorner = False
    if (mat[0][0] == player.color or mat[19][0] == player.color or mat[0][19] == player.color or mat[19][19] == player.color):
        isInCorner = True
    return isInCorner






while isEnd == False:

    #on trie la liste dans l'ordre de l'attribut couleur et on affiche l'ordre
    listOfPlayers.sort(key=lambda x: x.color)
    displayOrder(listOfPlayers)


    # on remplace toutes les matrices des pièces avec le numéro d'ordre du joueur
    replacePiecesWithGoodNumbers(listOfPlayers)
    print("--------------------------------\nDébut de la partie : " + listOfPlayers[0].name + " à toi de jouer !\n\nListe de tes pièces : ")





    isEndTurnOne = False
    isEndTurn = False
    goodCoords = False

    # turn 1
    while isEndTurnOne == False:
        for i in range (4):
            playerCurrent = listOfPlayers[i]
            displayListPieces(listOfPlayers[i].listPieces)
            displayMat(mat)
            idPiece = int(input("Numéro de la pièce souhaitée ? "))

            coords = str(input("Première pièce obligatoirement dans un coin !\nOù veux-tu poser ta pièce ? (coordonnées du carré le plus en haut à gauche) : "))
            print(i)
            for p in listOfPlayers[i].listPieces:
                if p.id == idPiece:
                    piece = p
            print(piece, mat, coords, playerCurrent)

            matTemp = copy.deepcopy(mat)
            mat = placePiece(piece, mat, coords, playerCurrent)
            while(checkPieceInCorner(mat, playerCurrent) == False):

                mat = [matTemp]
                displayMat(mat)
                coords = str(input("Première pièce obligatoirement dans un coin !\nOù veux-tu poser ta pièce ? (coordonnées du carré le plus en haut à gauche) : "))
                print(i)
                for p in listOfPlayers[i].listPieces:
                    if p.id == idPiece:
                        piece = p
                print(piece, mat, coords, playerCurrent)
                temp = mat
                mat = placePiece(piece, mat, coords, playerCurrent)
            displayMat(mat)

            coords = "none"
            if(i == 3):
                isEndTurnOne = True

    while isEndTurn == False:
        for i in range (4):
            playerCurrent = listOfPlayers[i]
            displayListPieces(listOfPlayers[i].listPieces)
            displayMat(mat)
            idPiece = int(input("Numéro de la pièce souhaitée ? "))

            coords = str(input("Où veux-tu poser ta pièce ? (coordonnées du carré le plus en haut à gauche) : "))
            print(i)
            for p in listOfPlayers[i].listPieces:
                if p.id == idPiece:
                    piece = p
            print(piece, mat, coords, playerCurrent)
            temp = mat
            mat = placePiece(piece, mat, coords, playerCurrent)

            while(checkPieceInCorner(mat, playerCurrent) == False):
                mat = temp
                coords = str(input("Première pièce obligatoirement dans un coin !\nOù veux-tu poser ta pièce ? (coordonnées du carré le plus en haut à gauche) : "))
                print(i)
                for p in listOfPlayers[i].listPieces:
                    if p.id == idPiece:
                        piece = p
                print(piece, mat, coords, playerCurrent)
                temp = mat
                mat = placePiece(piece, mat, coords, playerCurrent)
            displayMat(mat)

            coords = "none"
            if(i == 3):
                isEndTurnOne = True


    isEnd = True
    #






# for line in mat:
#     print (line)





i0 = 1


#i1 = Tk.PhotoImage(file="Z:\Projet_B\Carré_Blanc.png")



root = Tk()

#root.geometry("1920x1080")

# cnv=Canvas(root, width=4000, height=2000, bg="white")
# cnv.pack(padx=200, pady=200)

here = os.getcwd()
#print(here)
uri_carreoui = os.path.join(here + "\images\\11_bleu.png")
uriCB = os.path.join(here + "\images\\carre_blanc.png")
uriCN = os.path.join(here + "\images\carre_blanc.png")

#print(uriCB)

i0 = 0
# Création de l'objet PhotoImage :
if i0 == 0:
    i0 = PhotoImage(file=uriCB)
if i0 == 1:
    i0 = PhotoImage(file=uriCN)

# Affichage de l'image :
# Image_Affichee = cnv.create_image(500, 100, image = i0, anchor='nw')
# Image_Affichee = cnv.create_image(500, 200, image = i0, anchor='nw')

x=200
y=20
imgTest = ImageTk.PhotoImage(Image.open(uriCB))


# for i in range(10,30):
#     for j in range(10,30):
#         x = i * 25
#         y = j * 25
#         Label(root, image=imgTest).place(x=x, y=y)
        # if int(mat[i][j]) == 0:
        #     print("OUI", x, y)
        #     i0 = PhotoImage(file=uriCB)
        #     cnv.create_image(x, y, image=i0, anchor='nw')
        # else:
        #
        #     i0 = PhotoImage(file=uriCN)
        #     print("NON", x, y)
        #
        #     cnv.create_image(x, y, image=i0, anchor='nw')
        #cnv.create_image(x, y, image=i0, anchor='nw')

# for y in range(22):
#     for x in range(22):
#         #print(x, y)
#         a = y * 9
#         o = x * 9
#         #print(a)
#         #print(o)
#         i0 = (mat[y][x])
#         # Création de l'objet PhotoImage :
#         if i0 == 0:
#             i0 = PhotoImage(file='Z:\Projet_B\Carré_Blanc.png')
#         if i0 == 1:
#             i0 = PhotoImage(file='Z:\Projet_B\Carré_Noir.png')
#
#         Image_Affichee = cnv.create_image(a, o, image = i0, anchor='nw')


uri_carre = os.path.join(here + "\images\\6_vert.png")
uri_carre_de = os.path.join(here + "\images\\1_bleu.png")
i_test = PhotoImage(file=uri_carre)
i_test2 = PhotoImage(file=uri_carre_de)

#
# cnv.create_image(1000,100, image=i_test, anchor='nw')
# cnv.create_image(240,120, image=i_test2, anchor='nw')


def show_msg():
   messagebox.showinfo("Message","Hey There! I hope you are doing well.")

# # Add an optional Label widget
# Label(root, text= "Welcome Folks!", font= ('Aerial 17 bold italic')).place(x=200, y=200)
#
# # Create a Button to display the message
#

# Label(root, image = img).place(x=500, y=500)



# class SimpleApp():
#     def __init__(self, master, filename, **kwargs):
#         self.master = master
#         self.filename = filename
#         self.canvas = tk.Canvas(master, width=500, height=500)
#         self.canvas.pack()
#
#         self.update = self.draw().__next__
#         master.after(100, self.update)
#
#     def draw(self):
#         image = Image.open(self.filename)
#         angle = 0
#         for i in range (1000):
#             tkimage = ImageTk.PhotoImage(image.rotate(angle))
#             canvas_obj = self.canvas.create_image(
#                 250, 250, image=tkimage)
#             self.master.after_idle(self.update)
#             yield
#             self.canvas.delete(canvas_obj)
#             angle += 10
#             angle %= 360
#
#
# app = SimpleApp(root, uri_carreoui)


uri_carreoui = os.path.join(here + "\images\\16_bleu.png")
image = Image.open(uri_carreoui)
angle = 90
tkimage = ImageTk.PhotoImage(image.rotate(angle))

img = ImageTk.PhotoImage(Image.open(uri_carreoui))
Label(root, image=img).place(x=250, y=500)
Label(root, image=tkimage).place(x=1000, y=800)



# def callback(e):
#    x= e.x
#    y= e.y
#    print("Pointer is currently at %d, %d" %(x,y))
#    canvas.coords(x,y)
#
# img = Label(root, image=tkimage).place(x=500, y=500)
# canvas= Canvas(root, width= 1920, height= 1080)
# canvas.pack()
# canvas.bind('<Motion>',callback)
#
#
# canvas.create_image(960,540,image=img, anchor="center", tag="ship")

# p2 = Piece(5, [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], -1, "C:\\Users\\jocel\\OneDrive\\Bureau\\ESEO\\blokus\images\\15_bleu.png", 500,500)
#



#root.mainloop()

