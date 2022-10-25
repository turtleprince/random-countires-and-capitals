# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:54:01 2022

@author: turtl_4
"""


from tkinter import *
import random
root = Tk()
root.title("RANDOM COUNTRIES AND CAPITALS")
root.geometry("400x400")


entry_country_name = Entry(root)
entry_capital_name = Entry(root)

label_country_list = Label(root)
label_capital_list = Label(root)

label_country_name = Label(root)
label_capital_name = Label(root)

list1=["INDIA","NETHERLANDS","ITALY"]
list2=["New Delhi","Amsterdam","Rome"]


def country_name():
    length = len(list1)
    r_num = random.randint(0, length-1)
    label_country_name["text"] = "Your country name is: "+str(list1[r_num])
    label_capital_name["text"] = "Your capital name is: "+str(list2[r_num])
    
def add_name():
   country_name = entry_country_name.get();
   capital_name = entry_capital_name.get();
   list1.append(country_name)
   list2.append(capital_name)
   label_country_list["text"] = "Country Name : " + str(list1);
   label_capital_list["text"] = "Capital Name : " + str(list2); 
    
    
    
    

entry_country_name.place(relx=0.5, rely=0.1, anchor=CENTER)

entry_capital_name.place(relx=0.5, rely=0.2, anchor=CENTER)

label_country_list.place(relx=0.5, rely=0.3, anchor=CENTER)

label_capital_list.place(relx=0.5, rely=0.4, anchor=CENTER)

btn = Button(root,text="Add The country & Capital",command=add_name)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label_country_name.place(relx=0.5, rely=0.6, anchor=CENTER)

label_capital_name.place(relx=0.5, rely=0.7, anchor=CENTER)

btn2 = Button(root,text="Show Random Country & Capital", command=country_name)

btn2.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    
root.mainloop()