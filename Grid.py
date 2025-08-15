from tkinter import *
root = Tk()
mylabel1 = Label(root , text = "hello world")
mylabel2 = Label(root , text = "this is habiba")
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)
root.mainloop()
#end of the program
# to put some space in betwween the labels, we can use empty labels with spaces
from tkinter import *
root = Tk()
mylabel1 = Label(root , text = "hello world")
mylabel2 = Label(root , text = "this is habiba")
mylabel3 = Label(root , text = "                          ")
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=1,column=1)
root.mainloop()
#end of the program
