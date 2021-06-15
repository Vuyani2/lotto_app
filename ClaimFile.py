from tkinter import *
from tkinter import messagebox


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        lotto.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def clear_entry():

    fullName_entry.delete(0, 'end')
    Email_entry.delete(0, 'end')
    ID_entry.delete(0, 'end')


lotto = Tk()
lotto.title("Claim Prize")
lotto.geometry("500x600")
lotto.config(background='#fc0')


canvas = Canvas(lotto, width=312, height=167)
canvas.place(x=100, y=50)
img = PhotoImage(file="Ithuba-logo.jpg.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# labels& entries

head = Label(lotto, text="YOUR TICKET TO MILLIONNERS", font=("bold", 18), bg="#fc0", fg="black")
head.place(x=70, y=10)

fullname = Label(text="Full Name", fg="black", font=("bold", 15), bg="#fc0")
fullname.place(x=30, y=250)

fullName_entry = Entry(width=24, fg="black", font=("bold", 15))
fullName_entry.place(x=150, y=250)

Email = Label(text="Email", fg="black", font=("bold", 15), bg="#fc0")
Email.place(x=30, y=300)

Email_entry = Entry(width=24, fg="black", font=("bold", 15))
Email_entry.place(x=150, y=300)

ID = IntVar
ID_l = Label(text="ID number", fg="black", font=("bold", 15), bg="#fc0")
ID_l.place(x=30, y=350)

ID_entry = Entry(textvariable=ID, width=24, fg="black", font=("bold", 15))
ID_entry.place(x=150, y=350)


# button
reset_btn = Button(lotto, text='clear', bg='blue', command=clear_entry, borderwidth=5, width=10)
reset_btn.place(x=300, y=400)
btn = Button(lotto, text="Claim", bg="red", width=10, borderwidth=5)
btn.place(x=100, y=400)
exit_btn = Button(lotto, text='Exit', bg='green', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=300, y=450)

lotto.mainloop()