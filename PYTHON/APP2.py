# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
import sys
import random
import app3

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in app3.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in app3.search(FIRST_NAME_text.get(),LAST_NAME_text.get(),ADRESS_text.get(),TEL_text.get()):
        list1.insert(END,row)

def add_command():
    app3.insert(FIRST_NAME_text.get(),LAST_NAME_text.get(),ADRESS_text.get(),TEL_text.get())
    list1.delete(0,END)
    list1.insert(END,(FIRST_NAME_text.get(),LAST_NAME_text.get(),ADRESS_text.get(),TEL_text.get()))

def delete_command():
    app3.delete(selected_tuple[0])

def update_command():
    app3.update(selected_tuple[0],FIRST_NAME_text.get(),LAST_NAME_text.get(),ADRESS_text.get(),TEL_text.get())

def next_screen():
    mLabel1.place_forget()
    mbutton.place_forget()
#
window=Tk()
window.title("**ElectricaL-GReece**")
window.geometry("420x350")
window.config(background="#a1dbcd")

#LABEL
l1=Label(window,text="FIRST_NAME",font = "Arial 8  bold", border= 6).grid(row=0,column=0)
#
l2=Label(window,text="LAST_NAME",font = "Arial 8 bold", border= 6 ).grid(row=1,column=0)
#
l3=Label(window,text="ADRESS",font = "Arial 8  bold", border= 6 ).grid(row=0,column=2)
#
l4=Label(window,text="TEL",font = "Arial 8 bold", border= 6 ).grid(row=1,column=2)
#TEXT
FIRST_NAME_text=StringVar()
e1=Entry(window,textvariable=FIRST_NAME_text,border= 6,font = "Arial 8 bold",).grid(row=0,column=1)
#
LAST_NAME_text=StringVar()
e2=Entry(window,textvariable=LAST_NAME_text,border= 6,font = "Arial 8 bold").grid(row=1,column=1)
#
ADRESS_text=StringVar()
e3=Entry(window,textvariable=ADRESS_text,border= 6,font = "Arial 8 bold").grid(row=0,column=3)
#
TEL_text=StringVar()
e4=Entry(window,textvariable=TEL_text,border= 6,font = "Arial 8 bold").grid(row=1,column=3)
#
                 
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=8)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)
                 
list1.bind('<<ListboxSelect>>',get_selected_row)
                 
#BUTTONS
b1=Button(window,text="View all", width=12, border= 6,command=view_command).grid(row=2,column=3)

b2=Button(window,text="Search ", width=12, border= 6,command=search_command).grid(row=3,column=3)

b3=Button(window,text="Add Entry", width=12, border= 6,command=add_command).grid(row=4,column=3)

b4=Button(window,text="Update", width=12, border= 6,command=update_command).grid(row=5,column=3)

b5=Button(window,text="Delete", width=12, border= 6,command=delete_command ).grid(row=6,column=3)

b6=Button(window,text="Close", width=12, border= 6,command=window.destroy).grid(row=7,column=3)

window.mainloop()
