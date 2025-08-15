from tkinter import *
# This code creates a simple Tkinter application with an Entry widget.
root = Tk()
e = Entry(root)
e.pack()
root.mainloop()

# This code creates an Entry widget with specific properties.
root = Tk()
e = Entry(root,width=50, bg='lightblue', fg='black',borderwidth=5)
e.pack()
root.mainloop()

# This code creates an Entry widget with a default text.
root = Tk()
e = Entry(root)
e.pack()
e.insert(0, "Enter your Name:")
root.mainloop()

# Entry widget and a Button that displays a greeting message when clicked.
root = Tk()
e = Entry(root,width=50)
e.pack()
e.insert(0, "Enter your Name:")
def myClick():
    Hello = "Hello " + e.get()
    mylabel = Label(root , text=Hello)
    mylabel.pack()
myButton = Button(root, text="Click Me", command=myClick)
myButton.pack()
root.mainloop() 