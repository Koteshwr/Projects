from tkinter import *
import requests as r
import json as j
import pprint as p
from tkinter import messagebox as msg

        
def fun(moivie_name):
    global a
    global rating
    global rt
    global dol
    global rs
    
    try:
        movie=a.get()
        print(movie)
        data = r.get('https://omdbapi.com/?i=tt3896198&apikey=e6684083&t='+movie)
        text = j.loads(data.text)
        p.pprint(text)
        data1 = r.get('http://data.fixer.io/api/latest?access_key=0815ea615872c1e2d9bc083f714c92a8')
        text1 = j.loads(data1.text)
        b=text['BoxOffice']
        b=b.lstrip('$')
        b=b.split(',')
        b=int(''.join(b))
        inr = (b/text1['rates']['USD'])*(text1['rates']['INR'])


        dol.set(text['BoxOffice'])
        rs.set(inr)
        rating.set(text["Ratings"][0]['Value'])
        rt.set(text['Ratings'][1]['Value'])
    except KeyError:
        msg.showerror("Error",f"SORRY!!!!\nThe Movie you are Searching for is not Found")
        dol.set("0")
        rs.set("0")
        rating.set("0/10")
        rt.set("0%")
    except ConnectionError:
        msg.showerror("ConnectionError","Check Your Internet Connection")
    except r.exceptions.ConnectionError:
         msg.showerror("ConnectionError","Check Your Internet Connection")

root = Tk()
root.geometry("410x530")
root.title("MOVIES GUI")
root.resizable(False,False)


a = StringVar()
rating = StringVar()
rt = StringVar()
dol = StringVar()
rs = IntVar()

f= Frame(root,background="blue")
Label(f,text="Welcome to My New GUI\n Here you can Search for Your favourite movie details",font="verdana 10 bold").pack()
Label(f,text="Enter the Movie Name :",font="verdana 14 bold").pack(padx=10,pady="10")
Entry1=Entry(f,textvariable=a,borderwidth=4,font="verdana 20").pack(padx="20",pady="10")
f.pack(pady="20")
b=Button(root,text="Search For Movie Details",font="verdana 10 bold",borderwidth="5",background="blue",command=fun,padx="30",pady="10")
b.pack(pady="5")



f_1=Frame(root)

f2=Frame(f_1,background="blue")
Label(f2,text="Ratings  : ",font="verdana 13 bold").pack(side=LEFT,padx="10",pady="10")
rating.set("0/10")
Entry2 = Entry(f2,textvariable=rating,borderwidth=4,font="verdana 15").pack(side=RIGHT,padx="10",pady="10")

f2.pack()

f3=Frame(f_1,background="blue")
Label(f3,text="Rotten tomatoes: ",font="verdana 10 bold").pack(side=LEFT,padx="5",pady="10")
rt.set("0%")
Entry3 = Entry(f3,textvariable=rt,borderwidth=4,font="verdana 15").pack(side=RIGHT,padx="5",pady="10")

f3.pack()
f_1.pack()


f_2=Frame(root)

f4=Frame(f_2,background="blue")
Label(f4,text="BoxOffice in $: ",font="verdana 11 bold").pack(side=LEFT,padx="5",pady="10")
dol.set(0)
Entry2 = Entry(f4,textvariable=dol,borderwidth=4,font="verdana 15").pack(side=RIGHT,pady="10")

f4.pack()

f5=Frame(f_2,background="blue")
Label(f5,text="BoxOffice in rs: ",font="verdana 10 bold").pack(side=LEFT,padx="5",pady="10")
rs.set(0)
Entry3 = Entry(f5,textvariable=rs,borderwidth=4,font="verdana 15").pack(side=RIGHT,padx="5",pady="10")

f5.pack()
f_2.pack()
Button(root,text="Click here to EXIT >>>",font="verdana 10 bold italic",command=exit,borderwidth=5,background="blue").pack(pady=10)

root.mainloop()