from tkinter import *

window = Tk()

window.title("Miles to Kilometers Converter")
window.minsize(width=250,height=150)
window.config(padx=20,pady=20)

#function to convert input to km

def convert():
    final_sum = int(input.get()) * 1.60934
    converted_miles["text"] = final_sum

#0/0

#0/1

input = Entry()
input.config(width = 10)
input.grid(column=1, row=0)

#0/2

miles = Label(text="Miles")
miles.grid(row=0, column=2)
miles.config(padx=5, pady=5)

#1/0

is_equal_to = Label(text="is equals to:")
is_equal_to.grid(row=1,column=0)
is_equal_to.config(padx=5,pady=5)

#1/1
converted_miles = Label(text=0)
converted_miles.grid(row=1,column=1)
converted_miles.config(padx=5,pady=5)

#1,2

km = Label(text="Km")
km.grid(row=1,column=2)
km.config(padx=5,pady=5)

#2,0

#2,1

calculate_button = Button(text="Calculate", command = convert)
calculate_button.grid(column=1,row=2)
calculate_button.config(padx=5, pady=5)

#2,2


#program layout
#0,0 empty
#0,1 Entry input miles
#0,2 Label miles
#1,0 Label is equal to
#1,1 Label display output
#1,2 Label Km
#2,0 empty
#2,1 Button
#2,2 empty
#           |       Input      | Miles
# isequalto |   Display input  | Km
#           | Calculate button |

window.mainloop()
