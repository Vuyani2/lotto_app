from tkinter import *
import random
import tkinter.ttk
from tkinter import messagebox


def verify():
    pass





windows = Tk()
windows.title("Lotto Draw")
windows.geometry("650x600")
windows.config(background="yellow")

canvas = Canvas(windows, width=312, height=167)
canvas.place(x=400, y=50)
img = PhotoImage(file="Ithuba-logo.jpg.png")
canvas.create_image(0, 0, anchor=NW, image=img)

lottries = Label(windows, text="PANDA PUSHA PLAY", font=("bold", 20), bg="yellow", fg="black")
lottries.place(x=200, y=20)

play = Label(windows, text="Play!! :", font=("bold", 12), bg="black", fg="white")
play.place(x=300, y=80)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()


#canvas=Canvas(windows,width=40,height=40)
#canvas.grid(row=1,column=1)
#img=ImageTk.PhotoImage(Image.open("lotto.png"))
#canvas.create_image(0,-50,image=img)

txt1 = Spinbox(windows, from_=1, to=49, textvariable=num1, width=2, font=("bold", 20))
txt1.place(x=30, y=150)
txt2 = Spinbox(windows, from_=1, to=49, textvariable=num2, width=2, font=("bold", 20))
txt2.place(x=100, y=150)
txt3 = Spinbox(windows, from_=1, to=49, textvariable=num3, width=2, font=("bold", 20))
txt3.place(x=170, y=150)
txt4 = Spinbox(windows, from_=1, to=49, textvariable=num4, width=2, font=("bold", 20))
txt4.place(x=240, y=150)
txt5 = Spinbox(windows, from_=1, to=49, textvariable=num5, width=2, font=("bold", 20))
txt5.place(x=310, y=150)
txt6 = Spinbox(windows, from_=1, to=49, textvariable=num6, width=2, font=("bold", 20))
txt6.place(x=380, y=150)
result_answer = Label(windows, width=50, height=8)
result_answer.place(x=150, y=300)


def exitapplication():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        windows.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def claim():
    messagebox.showinfo("Alert", "Thank you for playing")
    windows.destroy()
    import ClaimFile


def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    my_list = [x, y, z, a, b, c]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) < 50:
        messagebox.showinfo("hurray", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(text="Jackpot Hurray \n" + "You just got your self Price : R10, 000 000.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
            elif len(same) == 5:
                result_answer.config(text="Felicitations" + "You got 5 numbers correct" + "\n With this Outstanding Achievement" + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
            elif len(same) == 4:
                result_answer.config(text="Felicitations" + "You got 4 numbers correct" + "\n With this Meritorious Achievement" + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
            elif len(same) == 3:
                result_answer.config(text="Felicitations" + "You got 3 numbers correct" + "\n With this Substantial Achievement" + "You won yourself R100.50" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
            elif len(same) == 2:
                result_answer.config(text="Felicitations" + "You got 2 numbers correct" + "\n With this Adequate Achievement" + "You won yourself R20.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
            elif len(same) == 1:
                messagebox.showinfo("RESULT", "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
    else:
        messagebox.showinfo("NOOO", "Follow the rules")
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num4.delete(0, END)
        num5.delete(0, END)
        num6.delete(0, END)


btn = Button(windows, text="CHECK YOUR RESULTS", bg="magenta", command=luck)
btn.place(x=250, y=250)
exit_btn = Button(windows, text='Exit', bg='#8dc63f', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=500, y=450)
claimbtn=Button(windows, text='Claim Prize', bg='#8dc63f', command=claim, borderwidth=5, width=10, state="disable")
claimbtn.place(x=500, y=500)
windows.mainloop()
