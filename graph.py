from tkinter import *

root = Tk()
root.geometry("1000x800")


cv = Canvas(root, width = 1000, height = 800)
cv.pack()

cv.create_rectangle(100, 100, 900, 500, fill = "black")


for i in range(32):
    for j in range(16):
        cv.create_oval(100 + i*25, 100 + j * 25, 125 + i * 25, 125 + j * 25, fill = "white")


root.mainloop()
