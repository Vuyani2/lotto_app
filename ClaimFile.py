from tkinter import *
from tkinter import messagebox


#def clear_entry():
 #   userentry.delete(0, 'end')
  #  entrypass.delete(0, 'end')



root = Tk()
root.title("Password and username Verification")
root.geometry("500x400")
root.config(bg='yellow')


frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)
exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=lambda: root.destroy())
exit_btn.grid(row=5, column=2, pady=5)
headlbl=Label(frame, text="ADD BANKING DETAILS", font=("bold", 20), bg="yellow", fg="black")

#cal_btn = Button(frame, text='Send', bg='#8dc63f', command=verify)
#cal_btn.grid(row=5, column=1, pady=5)

root.mainloop()