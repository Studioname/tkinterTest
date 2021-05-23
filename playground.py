from tkinter import *

window = Tk()

window.title("First gui program")

window.minsize(width=500,height=500)

#labels
#labels are static text printed to the screen, although they are changeable

my_label = Label(text="I am a label", font = ("Arial", 24))

#packing
#every element must be packed in order to show on the screen

my_label.pack()

#buttons
#buttons can be made to do a variety of things

def button_clicked():
    my_label["text"] = input.get()

button = Button(text = "Click me", command=button_clicked)
button.pack()

#entry
#entry is for taking user input

input = Entry(width = 10)
input.pack()

#to return a value from an input, get() returns the input as a string

print(input.get())

#text
#text is for text boxes. focus put the cursor in the text box, insert() puts some text in there. END
#puts the text in there as an existing string

text = Text(height = 5, width = 30)
text.focus()
text.insert(END,"Hello there")
text.pack()

#spinbox
#spinbox is a little number wheel which you can click up or down
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#scale
#creates a sliding scale [note that the 'from_' keyword argument has an underscore

def scale_used(value):
    print(value)

scale = Scale(from_=0,to=100,width=5, command=scale_used)
scale.pack()

#checkbutton
#basically an on or off switch

def checkbutton_used():
    print(checked_state.get())

#checked state holds an int variable, 1 for on 0 for off

checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
checkbutton.pack()

#radiobutton
#a range of options, if they share a similar variable then only one can be true
#what's happening is that when a button is clicked, the keyword argument 'value' is being assigned to the
#keyword argument 'variable', and since both buttons share the same variable, only one of them can be true.
#If they had different variables, then more than one could be clicked at the same time

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio1 = Radiobutton(text="Option 1", value=1, variable = radio_state, command = radio_used)
radio2 = Radiobutton(text="Option 2", value=2, variable = radio_state, command = radio_used)
radio1.pack()
radio2.pack()

#listbox
#box containing a list
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Banana", "Orange"]
#fruits are inserted into listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<Listbox Select>>", listbox_used)
listbox.pack()




window.mainloop()




# def argsum(*args):
#     return sum(args)
#
# print(argsum(1,2,3,4,5,6))
#
# def calculator(n, **kwargs):
#     n += kwargs.get("add")
#     n *= kwargs.get("multiply")
#     n -= kwargs.get("minus")
#     n /= kwargs.get("divide")
#     return n
#
# print(calculator(1,add=4, multiply=10, minus= 50, divide=2))
#
# class Falafel:
#     def __init__(self, **kwargs):
#         self.onions = kwargs.get("onions")
#         self.cooked = kwargs.get("cooked")
#         self.weight = kwargs.get("weight")
#
# my_falafel = Falafel(onions=True, cooked=True, weight= 500)
# print(my_falafel.onions, my_falafel.cooked, my_falafel.weight)

