#simple flight booking code

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x500")

Label(root, text="Which country you want to travel in?",
      font="lucidia 19 bold").pack()

country = ["Australia","Japan","Nepal","India","England","Italy"]

var = StringVar()

new_var = var.set("nonewhere")

def travel():
    tmsg.showinfo("Let's travel.We are booking your flight to {}.".format(var.get()))
    
for x in range(6):
    Radiobutton(root, text=country[x], variable=var, value=country[x]).pack()

Button(root, text="Let's travel",command=travel).pack()
root.mainloop()
