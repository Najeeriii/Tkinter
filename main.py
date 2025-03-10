from tkinter import *

window = Tk()
window.title('Tkinter Sample WIndow')
window.geometry('300x300')

#Label
greeting = Label(text="Hello User", fg='black', bg='white')
#Button
button = Button(text="Click here", bg='black', fg='blue')
#Entry
entry = Entry(fg="yellow", bg='green', width=40)

greeting.pack()
button.pack()
entry.pack()
window.mainloop()