# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



from tkinter import *
from tkinter import ttk


main = Tk()

main.geometry("500x500")

main.title("Scratchpad")

txt = Text(main,width=50,height=20)
txt.place(relx=0.5, rely=0.5, anchor=CENTER)

main.mainloop()





