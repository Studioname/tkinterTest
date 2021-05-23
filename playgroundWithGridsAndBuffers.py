from tkinter import *

window = Tk()

window.title("First gui program")

window.minsize(width=500,height=500)

#add padding between the edge of the window and elements

window.config(padx=50, pady=50)

#labels
#labels are static text printed to the screen, although they are changeable

my_label = Label(text="I am a label", font = ("Arial", 24))

#placing elements on screen
#every element must be placed on the screen using one of three methods: .pack() [not precise], .place() [very precise],
# or .grid() [middle of the road]

my_label.grid(column = 0, row = 0)

#padding can also be applied to elements

my_label.config(padx=50,pady=50)

#buttons
#buttons can be made to do a variety of things

def button_clicked():
    my_label["text"] = input.get()

button = Button(text = "Click me", command=button_clicked)
button.grid(column=1,row=1)

def second_button_clicked():
    print("Second button clicked")

second_button = Button(text = "Or click me", command=second_button_clicked)
second_button.grid(column=2,row=0)

#entry
#entry is for taking user input

input = Entry(width = 10)
input.grid(column=3,row=2)

#to return a value from an input, get() returns the input as a string




window.mainloop()