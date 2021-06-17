from tkinter import *
from tkinter import messagebox
import tkinter as tk
import main


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        lotto.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def clear_entry():

    accno_entry.delete(0, 'end')
    Acctype_entry.delete(0, 'end')
    institution_entry.delete(0, 'end')
    accName_entry.delete(0, 'end')


class player:
    def __init__(self,fullname,email,ID_NO,prize):
        self.prize = prize
        self.ID_NO = ID_NO
        self.email = email
        self.fullname = fullname



lotto = Tk()
lotto.title("Claim Prize")
lotto.geometry("600x600")
lotto.config(background='#fc0')


canvas = Canvas(lotto, width=312, height=167)
canvas.place(x=150, y=50)
img = PhotoImage(file="Ithuba-logo.jpg.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# labels& entries

head = Label(lotto, text="ACCOUNT DETAILS", font=("bold", 18), bg="#fc0", fg="black")
head.place(x=200, y=10)

accname = Label(text="Account Name", fg="black", font=("bold", 15), bg="#fc0")
accname.place(x=30, y=250)

accName_entry = Entry(width=24, fg="black", font=("bold", 15))
accName_entry.place(x=250, y=250)

accno = Label(text="Account Number", fg="black", font=("bold", 15), bg="#fc0")
accno.place(x=30, y=300)

accno_entry = Entry(width=24, fg="black", font=("bold", 15))
accno_entry.place(x=250, y=300)
Acctype_l = Label(text="Account Type", fg="black", font=("bold", 15), bg="#fc0")
Acctype_l.place(x=30, y=350)

OptionList = ["Savings Account", "Current Account", "Fixed / Deposit accounts", "Cheque Account"]
variable = tk.StringVar(lotto)
Acctype_entry = OptionMenu(lotto, variable, *OptionList)
Acctype_entry.config(width=30, font=('Helvetica', 12))
Acctype_entry.place(x=250, y=350)


OptionList2 = ["Absa", "Capitec bank", "Standard Bank", "NedbAnk", "FNB Bank"]
variable = tk.StringVar(lotto)
institution_entry = OptionMenu(lotto, variable, *OptionList2)
institution_entry.config(width=30, font=('Helvetica', 12))
institution_entry.place(x=250, y=400)

institution = Label(text="Institution", fg="black", font=("bold", 15), bg="#fc0")
institution.place(x=30, y=400)

#institution_entry = Entry(width=24, fg="black", font=("bold", 15))
#institution_entry.place(x=250, y=400)


# button
reset_btn = Button(lotto, text='clear', bg='blue', command=clear_entry, borderwidth=5, width=10)
reset_btn.place(x=300, y=450)
btn = Button(lotto, text="Claim", bg="red", width=10, borderwidth=5)
btn.place(x=100, y=450)
exit_btn = Button(lotto, text='Exit', bg='green', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=300, y=500)

lotto.mainloop()