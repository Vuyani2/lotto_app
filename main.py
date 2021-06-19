import json
from tkinter import *
import random
import tkinter.ttk
from tkinter import messagebox
from playsound import playsound


def verify():
    pass


windows = Tk()
windows.title("Lotto Draw")
windows.geometry("500x600")
windows.config(background="#fc0")

canvas = Canvas(windows, width=312, height=167)
canvas.place(x=70, y=20)
img = PhotoImage(file="Ithuba-logo.jpg.png")
canvas.create_image(0, 0, anchor=NW, image=img)


play = Label(windows, text="play lotto here :", font=("bold", 12), bg="#fc0", fg="white")
play.place(x=150, y=200)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()


txt1 = Spinbox(windows, from_=1, to=49, textvariable=num1, width=2, font=("bold", 20))
txt1.place(x=30, y=250)
txt2 = Spinbox(windows, from_=1, to=49, textvariable=num2, width=2, font=("bold", 20))
txt2.place(x=100, y=250)
txt3 = Spinbox(windows, from_=1, to=49, textvariable=num3, width=2, font=("bold", 20))
txt3.place(x=170, y=250)
txt4 = Spinbox(windows, from_=1, to=49, textvariable=num4, width=2, font=("bold", 20))
txt4.place(x=240, y=250)
txt5 = Spinbox(windows, from_=1, to=49, textvariable=num5, width=2, font=("bold", 20))
txt5.place(x=310, y=250)
txt6 = Spinbox(windows, from_=1, to=49, textvariable=num6, width=2, font=("bold", 20))
txt6.place(x=380, y=250)
result_answer = Label(windows, width=50, height=8)
result_answer.place(x=30, y=300)


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

    my_list = [int(x), int(y), int(z), int(a), int(b), int(c)]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))
    print(any(my_list))


    if any(my_list) < 0 or any(my_list) > 50:
        messagebox.showinfo("NOOO", "Follow the rules")

    else:
        messagebox.showinfo("hurray", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(
                    text="Jackpot Hurray \n" + "You just got your self Price : R10, 000 000.00" +
                         "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
                price = 10000000
                playsound('winlotto.mp3')
            elif len(same) == 5:
                result_answer.config(
                    text="Felicitations" + "You got 5 numbers correct" + "\n With this Outstanding Achievement" +
                         "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
                price = 8584
                playsound('winlotto.mp3')
            elif len(same) == 4:
                result_answer.config(
                    text="Felicitations" + "You got 4 numbers correct" + "\n With this Meritorious Achievement" +
                         "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
                price = 2384
                playsound('winlotto.mp3')
            elif len(same) == 3:
                result_answer.config(
                    text="Felicitations" + "You got 3 numbers correct" + "\n With this Substantial Achievement" +
                         "You won yourself R100.50" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
                price = 100.50
                playsound('winlotto.mp3')
            elif len(same) == 2:
                result_answer.config(
                    text="Felicitations" + "You got 2 numbers correct" + "\n With this Adequate Achievement" +
                         "You won yourself R20.00" + "\n Today Lotto Numbers are" + str(todaylotto))
                claimbtn["state"] = "normal"
                price = 20
                playsound('winlotto.mp3')
            elif len(same) == 1:
                messagebox.showinfo("RESULT",
                                    "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
                price = 0
                playsound('losinglotto.mp3')
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
                price = 0
                playsound('losinglotto.mp3')

        draw_list = {
            "my list": my_list,
            "winning prize": price,
            "todays lotto": todaylotto
        }

        draw_list = json.dumps(draw_list)

        print(draw_list)
        print(type(draw_list))

        with open("player_info.txt", "a+") as text_file:
            text_file.write(draw_list)


        return price



btn = Button(windows, text="CHECK YOUR RESULTS", bg="red", command=luck, borderwidth=5, width=15)
btn.place(x=100, y=450)
exit_btn = Button(windows, text='Exit', bg='green', command=exitapplication, borderwidth=5, width=10)
exit_btn.place(x=300, y=500)
claimbtn = Button(windows, text='Claim Prize', bg='blue', command=claim, borderwidth=5, width=10, state="disable")
claimbtn.place(x=300, y=450)
windows.mainloop()
