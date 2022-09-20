from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("VirBroGUI")

photo = PhotoImage(file = "C:\\Users\\DELL\\Desktop\\myWorkSpace\\virbroo\\images\\6ba174bf48e9b6dc8d8bd19d13c9caa9.gif")
label = Label(image = photo)
label.pack()
root.mainloop()

