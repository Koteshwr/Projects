import requests as r
import json as j
import re
from tkinter import *
from tkinter import messagebox as msg






def verifyph(ph):
    p1 = re.compile(r'(\+[0-9]?[0-9]?)?([- \s]?)(\d{3})([- \s]?)(\d{3})([- \s]?)(\d{4})')
    res = p1.search(ph)
    if res:
        return 1
    else:
        return 0






def result():
    global otp
    global name
    sid=EnterDetails.data["Details"]
    urlv=f'https://2factor.in/API/V1/{key}/SMS/VERIFY/{sid}/{otp.get()}'
    ver=r.get(urlv)
    vdata = j.loads(ver.text)
    if(vdata['Details']=='OTP Matched'):
        msg.showinfo("Result",f"Hello {name.get()} \nYour Login is Successful")
    else:
        msg.showerror("Result",f"Sorry {name.get()}\nOTP is invalid!!!\nTRY AGAIN")



def EnterDetails():
    global ph
    global GenOtp
    global otp
    global key
    phno=ph.get()
    print("phone number entered : ",phno)
    
    i=verifyph(phno)
    if(i==0):
        msg.showerror("error","You have entered invalid mobile number....")
        ph.set("")  
    else:     
        try:

            url1=f'https://2factor.in/API/V1/{key}/SMS/{phno}/AUTOGEN'
            res = r.get(url1)
            GenOtp.set("OTP Sent")
            EnterDetails.data = j.loads(res.text)
        except ConnectionError:
            msg.showerror("ConnectionError","Check Your Internet Connection")
        except r.exceptions.ConnectionError:
            msg.showerror("ConnectionError","Check Your Internet Connection")

    

key='189e7367-cdfc-11ec-9c12-0200cd936042'

root = Tk()
root.geometry("300x500")
root.title("LOGIN PORTAL")
ph = StringVar()
name=StringVar()
GenOtp=StringVar()
GenOtp.set("Generate OTP")
otp=StringVar()

Label(root,text="OTP Verification GUI",font="arial 20 bold").pack(pady=10)
f=Frame(root,background="orange")
Label(f,text="Enter your Name:",font="arial 14 bold").pack(pady=10)
Entry(f,textvariable=name,font="arial 20 bold",borderwidth=5).pack()
Label(f,text="Enter your mobile number:",font="arial 14 bold").pack(pady=10)
E = Entry(f,textvariable=ph,font="arial 20 bold",borderwidth=5)
E.pack()
Button(f,textvariable=GenOtp,font="arial 12 bold italic",background="green", borderwidth=2,command=EnterDetails).pack(pady=5)
Label(f,text="Enter the OTP you have received",font="arial 14 bold").pack(pady=10)
Entry(f,textvariable=otp,font="arial 20 bold",borderwidth=5).pack(pady=5)
Button(f,text="VERIFY",font="arial 11 bold italic",background="green", borderwidth=2,command=result).pack(pady=5)

f.pack()
Button(root,text="Click here to EXIT >>>",font="arial 11 bold italic",command=exit,borderwidth=3,background="orange").pack(pady=5)
root.mainloop()