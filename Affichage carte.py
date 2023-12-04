from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from tkinter import * 
from PIL import Image, ImageTk



fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

#carte 0
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_0.svg")
renderPM.drawToFile(drawing, "temp_0.png", fmt="PNG")

img0 = Image.open('temp_0.png')
photo0 = ImageTk.PhotoImage(img0)
size = img0.size

#carte 1
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_1.svg")
renderPM.drawToFile(drawing, "temp_1.png", fmt="PNG")

img1 = Image.open('temp_1.png')
photo1 = ImageTk.PhotoImage(img1)
size = img1.size

#carte 2
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_2.svg")
renderPM.drawToFile(drawing, "temp_2.png", fmt="PNG")

img2 = Image.open('temp_2.png')
photo2 = ImageTk.PhotoImage(img2)
size = img2.size

#carte 3
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_3.svg")
renderPM.drawToFile(drawing, "temp_3.png", fmt="PNG")

img3 = Image.open('temp_3.png')
photo3 = ImageTk.PhotoImage(img3)
size = img3.size

#carte 5
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_5.svg")
renderPM.drawToFile(drawing, "temp_5.png", fmt="PNG")

img5 = Image.open('temp_5.png')
photo5 = ImageTk.PhotoImage(img5)
size = img5.size

#carte 8
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_8.svg")
renderPM.drawToFile(drawing, "temp_8.png", fmt="PNG")

img8 = Image.open('temp_8.png')
photo8 = ImageTk.PhotoImage(img8)
size = img8.size

#carte 13
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_13.svg")
renderPM.drawToFile(drawing, "temp_13.png", fmt="PNG")

img13 = Image.open('temp_13.png')
photo13 = ImageTk.PhotoImage(img13)
size = img13.size

#carte 20
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_20.svg")
renderPM.drawToFile(drawing, "temp_20.png", fmt="PNG")

img20 = Image.open('temp_20.png')
photo20 = ImageTk.PhotoImage(img20)
size = img20.size

#carte 40
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_40.svg")
renderPM.drawToFile(drawing, "temp_40.png", fmt="PNG")

img40 = Image.open('temp_40.png')
photo40 = ImageTk.PhotoImage(img40)
size = img40.size

#carte 100
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_100.svg")
renderPM.drawToFile(drawing, "temp_100.png", fmt="PNG")

img100 = Image.open('temp_100.png')
photo100 = ImageTk.PhotoImage(img100)
size = img100.size

#carte Int
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_interro.svg")
renderPM.drawToFile(drawing, "temp_Int.png", fmt="PNG")

imgInt = Image.open('temp_Int.png')
photoInt = ImageTk.PhotoImage(imgInt)
size = imgInt.size

#carte cafe
drawing = svg2rlg("C:/Users/aperret8/Desktop/image/cartes_cafe.svg")
renderPM.drawToFile(drawing, "temp_cafe.png", fmt="PNG")

imgcafe = Image.open('temp_cafe.png')
photocafe = ImageTk.PhotoImage(imgcafe)
size = imgcafe.size

canvas = Canvas(fenetre,width=660, height=765) #format de la carte : largeur->165 hauteur->255
canvas.create_image(0, 0, anchor=NW, image = photo0) # 0
canvas.create_image(165, 0, anchor=NW, image = photo1) # 1
canvas.create_image(330, 0, anchor=NW, image = photo2) # 2
canvas.create_image(495, 0, anchor=NW, image = photo3) # 3
canvas.create_image(0, 255, anchor=NW, image = photo5) # 5
canvas.create_image(165, 255, anchor=NW, image = photo8) # 8
canvas.create_image(330, 255, anchor=NW, image = photo13) # 13
canvas.create_image(495, 255, anchor=NW, image = photo20) # 20
canvas.create_image(0, 510, anchor=NW, image = photo40) # 40
canvas.create_image(165, 510, anchor=NW, image = photo100) # 100
canvas.create_image(330, 510, anchor=NW, image = photoInt) # ? / Interogation
canvas.create_image(495, 510, anchor=NW, image = photocafe) # cafe
canvas.pack()

fenetre.mainloop()
