# Tkinter Student Register
from tkinter import *
from tkcalendar import Calendar, DateEntry

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)
label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=240, y=130)
label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root)
entry_2.place(x=240, y=180)
label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20,
            variable=var, value=2).place(x=290, y=230)
label_4 = Label(
    root, text="Age:", width=20, font=("bold", 10))
label_4.place(
    x=70, y=280)
entry_3 = Entry(
    root)
entry_3.place(
    x=240, y=280)
label_5 = Label(
    root, text="Reg. No.:", width=20, font=("bold", 10))
label_5.place(
    x=70, y=330)
entry_4 = Entry(
    root)
entry_4.place(
    x=240, y=330)
label_6 = Label(
    root, text="Address:", width=20, font=("bold", 10))
label_6.place(
    x=70, y=380)
entry_5 = Entry(
    root)
entry_5.place(
    x=240, y=380)
label_7 = Label(
    root, text="Email ID:", width=20, font=("bold", 10))
label_7.place(
    x=70, y=430)
entry_6 = Entry(
    root)
entry_6.place(
    x=240, y=430)
# Create a Label
label_8 = Label(
    root, text="Date of Birth", width=20, font=("bold", 10))
label_8.place(
    x=77, y=480)
# Create a Calendar using DateEntry
cal = DateEntry(root, width=16, background="magenta3",
                foreground="white", bd=2)
cal.place(
    x=240, y=480)
Button(root, text='Submit', width=20, bg='brown',
       fg='white').place(x=180, y=530)
# it is use for display the registration form on the rootdow
root.mainloop()
