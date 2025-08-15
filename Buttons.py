from tkinter import *
root = Tk()
# Create a button widget
myButton = Button(root , text = 'Click me')
myButton.pack()
root.mainloop()

# Create a button widget with padding 
myButton = Button(root , text = 'Click me' , padx = 20 , pady = 30 )
myButton.pack()
root.mainloop()

# Create a button widget with foreground and background colors
myButton = Button(root , text = 'Click me' , fg="red" , bg = "#00FF00")
myButton.pack()
root.mainloop()

# Create a button widget with a command that executes when clicked
def myClick():
    mylabel = Label(root,text = " look!! , i just clicked the button!")
    mylabel.pack()
myButton = Button(root , text = 'Click me' ,command = myClick , fg="red" , bg = "#00FF00")
myButton.pack()
root.mainloop()