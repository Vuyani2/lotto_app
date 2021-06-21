from tkinter import *
from tkinter import messagebox
import rsaidnumber
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# CLASS


class Player:

    def __init__(self, fulname, email, id_no, playee_id, date_played):
        self.ID_NO = id_no
        self.email = email
        self.fullname = fulname
        self.player_id = playee_id
        self.date_played = date_played

    def __str__(self):
        return "name: " + self.fullname + " email: " + self.email + " id number: " + self.ID_NO + " player id: " + \
               self.player_id + " date played: " + str(self.date_played)

    def make_dict(self):
        current_date = datetime.date.today()

        player_dict = {
            "full name": self.fullname,
            "email": self.email,
            "id number": self.ID_NO,
            "player id": self.player_id,
            "date played": current_date
        }


#   FUNCTIONS


def player_id(fullnm, id_param):
    pos = fullnm.find(" ")
    surname = fullnm[pos+1]
    name = fullnm[0]
    idsliced = id_param[slice(6, 10, 1)]
    idplayer = surname+name+idsliced

    return idplayer


def send_email():
    try:
        sender_email_id = 'vuyanilottoapp@gmail.com'
        receiver_email_id = Email_entry.get()
        password = "Vuya@2019"
        subject = "Lotto"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "Your Account has been verified. Thank you for using our Lotto Application"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
        return True
    except Exception:
        messagebox.showerror("Error", Exception)
        return False


def logins():

    id_ = rsaidnumber.parse(ID_entry.get())
    birth_year = id_.date_of_birth.year
    currentyaer = datetime.date.today().year
    log = currentyaer - birth_year
    if log >= 18:

        if send_email():
            # try:

            person = Player(fullName_entry.get(), Email_entry.get(), ID_entry.get(),
                            player_id(fullName_entry.get(), ID_entry.get()), datetime.date.today())
            print(type(str(person)))

            with open("text_files/player_info.txt", "a+") as file:
                file.write(str(person))
            lotto.destroy()
            import main
        else:
            messagebox.showerror("Error", "invalid Email, please make sure to put in a valid email Account")

    else:
        messagebox.showerror("NOTE!!", "Not for person under the age of 18")


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

# creating window


lotto = Tk()
lotto.title("SIGN UP")
lotto.geometry("500x600")
lotto.config(background='#fc0')


canvas = Canvas(lotto, width=312, height=167)
canvas.place(x=100, y=50)
img = PhotoImage(file="images/Ithuba-logo.jpg.png")
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
btn = Button(lotto, text="LOGIN", bg="red", command=logins, width=10, borderwidth=5)
btn.place(x=100, y=400)
exit_btn = Button(lotto, text='Exit', bg='green', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=300, y=450)


lotto.mainloop()
