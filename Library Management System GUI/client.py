from tkinter import *
import library_database as db

# create blank window
window = Tk()
window.title('Library App')

# setting window size
window.geometry('1000x500')


def add_book_dialog():
    global add_dialog
    global str_topic
    add_dialog = Toplevel(window)
    topic_label = Label(add_dialog, text = "Topic", font = ("Arial Bold",20))
    
    topic_label.grid(column = 0, row = 0)
    topic_txt = Entry(add_dialog, font = ("Arial",20))
    topic_txt.grid(column = 1, row = 0)

    author_label = Label(add_dialog, text = "Author", font = ("Arial Bold",20))
    author_label.grid(column = 0, row = 1)
    author_txt = Entry(add_dialog, font = ("Arial",20))
    author_txt.grid(column = 1, row = 1)

    
    str_topic = topic_txt.get()
    str_author = author_txt.get()


    add_btn = Button(add_dialog, text = "Add a book", bg = "red", fg = "black", font = ("Arial",20), command=lambda:add_book(1, 2))
    add_btn.grid(column = 1, row = 2)

def add_book(topic = str_topic, author = str_topic):
    print(topic, author)
    ##db.insert(topic, author)
    add_dialog.destroy()


add_btn = Button(window, text = "Add a book", bg = "red", fg = "black", 
font = ("Arial",20), command=add_book_dialog)
add_btn.grid(column = 1, row = 1)

window.mainloop()