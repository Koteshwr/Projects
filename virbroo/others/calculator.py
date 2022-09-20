from tkinter import *


def click(event):
    global a
    val=event.widget.cget("text")
    if val=="AC":
        val=a.set("")
    elif val=="=":
        if a.get().isdigit():
            val=int(a.get())
        else: 
            val=eval(a.get())
        a.set(val)
    elif val=="<-":
        print(a.get()[:-1])
        val=a.get()[:-1]
        val=a.set(val)
    a.set(a.get()+val)
    scr.update()

root =Tk()
root.geometry("560x600")
root.title("calculator GUI by kotesh")
root.configure(bg='Lavender')
Label(text="CALCULATOR GUI",font="lucida 15 bold").pack()


a=StringVar()
a.set("")
scr=Entry(root, textvar=a, font="lucida 19 bold",borderwidth=7)
scr.pack(fill=X)


f1=Frame(root,background="black")

b=Button(f1,text="7",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=0,column=0,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="8",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=0,column=1,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="9",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=0,column=2,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="/",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=0,column=3,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="4",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=1,column=0,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="5",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=1,column=1,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="6",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=1,column=2,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="*",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=1,column=3,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="1",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=2,column=0,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="2",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=2,column=1,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="3",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=2,column=2,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="-",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=2,column=3,padx=28,pady=15)
b.bind("<Button-1>",click)


b=Button(f1,text="OFF",font="lucida 10 bold",padx=25,pady=8)
b.grid(row=3,column=0,padx=28,pady=15)
b.bind("<Button-1>",quit)

b=Button(f1,text="0",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=3,column=1,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="<-",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=3,column=2,padx=28,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="+",font="lucida 19 bold",padx=25,pady=8)
b.grid(row=3,column=3,padx=28,pady=15)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,background="black")
b=Button(f1,text="=",font="lucida 19 bold",padx=40,pady=8)
b.grid(row=0,column=0,padx=30)
b.bind("<Button-1>",click)

b=Button(f1,text="AC",font="lucida 19 bold",padx=30,pady=8)
b.grid(row=0,column=1,padx=30)
b.bind("<Button-1>",click)
f1.pack()
root.mainloop()
