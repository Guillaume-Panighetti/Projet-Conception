from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

drawing = svg2rlg("safari-pinned-tab.f387b3f2.svg")
renderPM.drawToFile(drawing, "temp.png", fmt="PNG")

from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

img = Image.open('cartes.svg')
pimg = ImageTk.PhotoImage(img)
size = img.size

canvas = Canvas(fenetre,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre.mainloop()