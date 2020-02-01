from tkinter import *

root = Tk()
frame = Frame(root, cursor = 'dot')
frame.pack()

bottomframe = Frame(root, cursor = 'plus')
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red", bg = 'pink', relief = 'sunken')
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="green", fg="green", bg = 'yellow', relief= 'ridge')
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue",bg = 'violet', relief = 'solid',state = 'disabled',underline = 3)
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black", bg = 'white', relief = 'flat')
blackbutton.pack( side = BOTTOM)

root.mainloop()