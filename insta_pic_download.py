# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:38:02 2021

@author: SACHIN
"""
import tkinter as tk
from tkinter import ttk, filedialog
import instaloader
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
print ('sachin123')
app = tk.Tk()
app.geometry('350x300')
app.configure(padx=20, pady=20, background = 'black')
#photo1 = PhotoImage(file = 'instalogo2.gif')
#Label (app,image = photo1,bg = 'white').grid(row = 6, column =1)

User_var = tk.StringVar()

root=instaloader.Instaloader()
name = User_var.get()
print (User_var.get())

root=instaloader.Instaloader()

def getusername():
    print (User_Name.get())
    new_name = User_Name.get()
    print ('name is : ',len(new_name))
    User_Name.delete("0",tk.END)
    if len(new_name) != 0:
        try:
            temp = root.download_profile(new_name,profile_pic_only=True)
            temp
            messagebox.showinfo("Information","Downloading, Please Wait")
            messagebox.showinfo("Information","Image Saved!, Check the folder where exe is located")
            
        except Exception as e:
            messagebox.showinfo("Information","Checking for the Profile Please Wait")
            print (Exception) 
            print ('Not Found')
            messagebox.showerror("Error", "Sorry! Profile Doesn't Exists")
    else:
        pass

#---------------------User Name-----------------------#    
user_lable = ttk.Label(app,text = 'User Name :', width=12)
user_lable.grid(row=4, column = 1, pady=55, padx=20)

User_Name = ttk.Entry(app, width=30, textvariable=User_var)
User_Name.grid(row=4, column = 2, pady=55, padx=0)
#-----------------------------------------------------#
Load_Data = ttk.Button(app, text='Download', command  = getusername , width=3)
Load_Data.grid(row=5, column=1, pady=5, padx=0, columnspan = 4)
Load_Data.configure(width=10)

app.title("Instagram Profile Pic Downloader")
app.mainloop()