from operator import ge
from tkinter import *

# create blank window
window = Tk()
window.title('Jonathan App')

# setting window size
window.geometry('1000x500')

# create a label widget with font size
lbl = Label(window, text = "Hello This is Jonathan's App", font = ("Arial Bold",20))
lbl.grid(column = 0, row = 0)

# handle button click event  
# handles textbox
# has to be placed before the button
def clicked():
    sent = 'Hello '+ txt.get()
    lbl2 = Label(window, text = sent, font = ("Arial Bold",20))
    lbl2.grid(column = 0, row = 0)

    # lbl.configure(text = res)
    # print(selected.get())
    # prints to the terminal

# adding a button widget with colors
# why can't the bg change?
btn = Button(window, text = "Click Me", bg = "red", fg = "black", font = ("Arial",20), command=clicked)
btn.grid(column = 0, row = 2)
# puts it in the second column of the window

# get input using entry class
txt = Entry(window, font = ("Arial",20))
# use the grid function as usual to add it to the window
txt.grid(column = 0, row = 1)

# create a label widget with font size
lbl = Label(window, text = "Hello Select Size of Pizza", font = ("Arial Bold",20))
lbl.grid(column = 0, row = 0)

# Add radio buttons widgets
selected = IntVar()
rad1 = Radiobutton(window,text='Small', value=1, variable=selected, font = ("Arial",20))
rad2 = Radiobutton(window,text='Medium', value=2, variable=selected, font = ("Arial",20))
rad3 = Radiobutton(window,text='Large', value=3, variable=selected, font = ("Arial",20))

rad1.grid(column = 0, row = 4)
rad2.grid(column = 0, row = 5)
rad3.grid(column = 0, row = 6)

def check_selected():
    print(selected.get())

btn = Button(window, text = "Select A RadioButton", bg = "red", fg = "black", 
font = ("Arial",20), command=check_selected)
btn.grid(column = 0, row = 7)

# Add a Checkbutton widget
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text = 'Choose', var = chk_state, font = ("Arial",20))
chk.grid(column = 0, row = 8)
# set the checked state (var=_chk_state) by passing the checkvalue to the checkbutton
# use IntVar to set value to 0 or 1 instead of BooleanVar

def check_chk_state():
    print(chk_state.get())

btn = Button(window, text = "Select A Checkbox", bg = "red", fg = "black", 
font = ("Arial",20), command=check_chk_state)
btn.grid(column = 0, row = 9)

window.mainloop()