from tkinter import *
from time import *
root=Tk()
root.configure(bg="black")
root.geometry("300x150")
root.title("Digital clock GUI")
def clock():
	t=strftime("%H:%M:%S")
	b.set(t)
	a.update()
	a.after(200,clock)
	
Label(root,text="DIGITAL CLOCK GUI",font="lucida 13 bold underline",bg="black",fg="blue").pack(padx=10)

#Label(root,text="-------------------------------------------------",bg="black",fg="blue").pack()
b=IntVar()
b.set(" ")
a=Entry(root,textvariable=b,font="dg-clock 25 bold",justify=CENTER,width=10,fg="blue",bg="black",bd="5")
a.pack(padx=10,pady=5)
clock()

Button(root,text="EXIT",font="lucida 10 bold",bd=5,bg="black",fg="blue",command=quit).pack()
root.mainloop()
