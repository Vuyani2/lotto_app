from tkinter import *
from tkinter import messagebox
import tkinter as tk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import requests
from tkinter import ttk

# Exit button command


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        lotto.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')

# Clear button command


def clear_entry():

    accno_entry.delete(0, 'end')
    accName_entry.delete(0, 'end')


# Currency converter Api

url = "http://api.exchangeratesapi.io/v1/latest?access_key=fab4bca97cc9094b963030c6064ed5c2"
req = requests.get(url)
result = req.json()
rates = result['rates'].keys()

# Email sending After claiming


def convertor():
    with open("text_files/player_info.txt", "r", encoding='utf-8-sig', errors='ignore') as text_file:
        line = text_file.readline()
        position = line.find("winning prize")
        end_of_line = line[slice(position + 16, len(line))]
        amount = end_of_line.split(",")[0]

    with open("text_files/player_info.txt", "r", encoding='utf-8-sig', errors='ignore') as text_file:
        line = text_file.readline()
        position = line.find("email")
        end_of_line = line[slice(position + 7, len(line))]
        email = end_of_line.split(" ")[0]

    prize = float(amount)
    new_amnt = prize * result['rates'][lst.get()]  # converting currency

    sender_email_id = 'vuyanilottoapp@gmail.com'
    receiver_email_id = email
    password = "Vuya@2019"
    subject = "Wined Prize"
    msg = MIMEMultipart()
    msg['From'] = sender_email_id
    msg['To'] = receiver_email_id
    msg['Subject'] = subject
    body = "Thank you for playing you have Won yourself an amount of " + str(new_amnt) + " in your chosen currency " + \
           "\n your account name is : " + str(accName_entry.get()) + "\n your Account number is : " + \
           str(accno_entry.get())
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email_id, password)
    s.sendmail(sender_email_id, receiver_email_id, text)
    s.quit()

# creating window


lotto = Tk()
lotto.title("Claim Prize")
lotto.geometry("600x600")
lotto.config(background='#fc0')

# Image

canvas = Canvas(lotto, width=312, height=167)
canvas.place(x=150, y=50)
img = PhotoImage(file="images/Ithuba-logo.jpg.png")
canvas.create_image(0, 0, anchor=NW, image=img)


# labels& entries
lst = ttk.Combobox(lotto)
rates = list(rates)
lst["values"] = rates
lst.place(x=250, y=450, width=315)
lbl_lst = Label(text="Type of currency", font=("bold", 15), bg="#fc0", fg="black")
lbl_lst.place(x=30, y=450)
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


# button
reset_btn = Button(lotto, text='clear', bg='blue', command=clear_entry, borderwidth=5, width=10)
reset_btn.place(x=300, y=500)
btn = Button(lotto, text="Claim", bg="red", width=10, borderwidth=5, command=convertor)
btn.place(x=100, y=500)
exit_btn = Button(lotto, text='Exit', bg='green', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=300, y=550)

lotto.mainloop()
