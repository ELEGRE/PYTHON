from tkinter import *


window=Tk()
window.title("**ElectricaL-GReece**")
window.geometry("520x160")
window.configure(background="#a1dbcd")
#
def from_m():
    km=float(e2_value.get())*0.001
    ft=float(e2_value.get())*3.2808
    nmi=float(e2_value.get())*0.00054
    t1.insert(END,km)
    t2.insert(END,ft)
    t3.insert(END,nmi)
def clear():
    e2.delete(0,END)
    t1.delete(0.0, END)
    t2.delete(0.0, END)
    t3.delete(0.0, END)
    return
#   
e1=Label(window,text="m-->", font = "Arial 10  bold")
e1.grid(row=0,column=0)
#
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)
#buttons
b1=Button(window,padx=10, pady=10,bd=4,text="Convert",command=from_m, fg="#a1dbcd", bg="#383a39",font = "Arial 10  bold" )
b1.grid(row=0,column=2)
b2=Button(window,padx=10, pady=10,bd=4,text="Quit!!",command=window.destroy, fg="#a1dbcd", bg="#383a39", font = "Arial 10  bold" )
b2.grid(row=0,column=3)
b3=Button(window,padx=10, pady=10,bd=4,text="-->Clear!!",command=clear, fg="#a1dbcd", bg="#383a39")
b3.grid(row=3,column=3)
#km
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
e1=Label(window,text="-km-",bd=8, font = "Arial 10  bold")
e1.grid(row=2,column=0)
#ft
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
e1=Label(window,text="-ft-",bd=8, font = "Arial 10  bold")
e1.grid(row=2,column=1)
#nmi
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
e3=Label(window,text="-nmi-",bd=8, font = "Arial 10  bold")
e3.grid(row=2,column=2)
#
window.mainloop()
