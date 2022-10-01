from tkinter import *
import library_database as db

# create blank window
window = Tk()
window.title('Library App')

# setting window size
window.geometry('1000x500')

def get_selected_row(event):
    '''
    This function help use track the 
    item that is selected in the list box
    '''

    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)


def view_command():
    '''
    This function helps use populate the listbox 
    gotten from the database 
    '''
    list1.delete(0,END)
    for row in db.view_all():
        list1.insert(END,row)

def get_details():
    print(selected_tuple)


def add_book_dialog():
    '''
    This function create a new window where we can 
    add a new book to the database
    '''
    global add_dialog
    add_dialog = Toplevel(window)
    
    # Create label for Topic
    topic_label = Label(add_dialog, text = "Topic", font = ("Arial Bold",20))
    topic_label.grid(column = 0, row = 0)
        
    # Create entry for Topic
    topic_txt = Entry(add_dialog, font = ("Arial",20))
    topic_txt.grid(column = 1, row = 0)

    # Create label for author
    author_label = Label(add_dialog, text = "Author", font = ("Arial Bold",20))
    author_label.grid(column = 0, row = 1)
    
    # Create entry for Author
    author_txt = Entry(add_dialog, font = ("Arial",20))
    author_txt.grid(column = 1, row = 1)

    # Create Button it calls the add_book function to add a new book
    add_btn = Button(add_dialog, text = "Add a book", bg = "red", fg = "black", font = ("Arial",20), command=lambda:add_book(topic_txt.get(), author_txt.get()))
    add_btn.grid(column = 1, row = 2)


def update_book_dialog(id, topic, author):
    '''
    This function create a new window where we can 
    add a new book to the database

    This function takes 
    Params
    id: Id of the selected book
    topic: topic of the selected book
    author: author of the selected book
    '''
    global update_dialog
    update_dialog = Toplevel(window)

    # Create label for Topic
    topic_label = Label(update_dialog, text = "Topic", font = ("Arial Bold",20))
    topic_label.grid(column = 0, row = 0)
    
    # Create entry for Topic
    topic_txt = Entry(update_dialog, font = ("Arial",20))
    topic_txt.insert(END,topic) # Fill the entry with the selected book topic
    topic_txt.grid(column = 1, row = 0)

    # Create label for Author
    author_label = Label(update_dialog, text = "Author", font = ("Arial Bold",20))
    author_label.grid(column = 0, row = 1)
    
    # Create entry for Author
    author_txt = Entry(update_dialog, font = ("Arial",20))
    author_txt.insert(END,author)
    author_txt.grid(column = 1, row = 1)

    # Create Button to update existing Book
    add_btn = Button(update_dialog, text = "Update the book", bg = "red", fg = "black", 
    font = ("Arial",20), command=lambda:update_book(id, topic_txt.get(), author_txt.get()))
    add_btn.grid(column = 1, row = 2)

def add_book(topic, author):
    '''
    Takes the topic and author from the filled entries in the
    add_book_dialog and add it to the database 
    '''
    db.insert(topic, author)
    add_dialog.destroy()
    view_command()

def update_book(id, topic, author):
    '''
    Takes the topic and author from the filled entries in the
    add_book_dialog and add it to the database 
    '''
    db.update(id, topic, author)
    update_dialog.destroy()
    view_command()


# Button that calls the add book dialog to add a book to the DB
add_btn = Button(window, text = "Add a book", bg = "red", fg = "black", 
font = ("Arial",20), command=add_book_dialog)
add_btn.grid(row=2,column=3)

# Button that refresh the list box
view_btn = Button(window, text = "View all books", bg = "red", fg = "black", 
font = ("Arial",20), command=view_command)
view_btn.grid(row=3,column=3)

# Button that calls the update book diaglog
selected_btn = Button(window, text = "Update book", bg = "red", fg = "black", 
font = ("Arial",20), command=lambda:update_book_dialog(selected_tuple[0], selected_tuple[1], selected_tuple[2]))
selected_btn.grid(row=4,column=3)

# Listbox that holds the data of all the books
list1=Listbox(window, height=6,width=35)
list1.grid(row=0,column=0,rowspan=12,columnspan=2)

# Scrollbar that will control the Listbox
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# Bind the list to the function get_selected_row function
# So that we can get the current book selected 
list1.bind('<<ListboxSelect>>',get_selected_row)

# Configure the listbox and the scrollbar to work together
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# This allows us to populate the listbox on initial load
view_command()

# This Must be here for our windows to work
window.mainloop()