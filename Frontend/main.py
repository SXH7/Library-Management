from tkinter import *

root = Tk()
root.geometry('150x200')

root.title("Library Tables")

def open_window(window):
    if(window == "book"):
        import book_window

tab_book = Button(root, text="Open Book Table", command = lambda:open_window("book"))
tab_book.grid(column=1, row=1, padx=10, pady=10)

tab_member = Button(root, text="Open Member Table", command = lambda:open_window("member"))
tab_member.grid(column=1, row=2, padx=10, pady=10)

tab_issue = Button(root, text="Open Issue Table", command = lambda:open_window("issue"))
tab_issue.grid(column=1, row=3, padx=10, pady=10)


root.mainloop()
