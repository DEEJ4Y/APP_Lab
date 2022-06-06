from ctypes import alignment
from email.policy import default
import tkinter as tk
from tkinter import *

days = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31"
]

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

years = []

for i in range(1984, 2004):
    years.append(i)

primaryBackgroundColor = "#685bca"
primaryColor = "#FFFFFF"

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background=primaryBackgroundColor)
root.title('tk')
root.geometry('1280x680')

l1 = tk.Label(root, text="FIRST NAME")
l1.grid(row=0)
t1 = tk.Entry(root)
t1.grid(row=0, column=1)
h1 = tk.Label(root, text="(max 30 characters a-z and A-Z)")
h1.grid(row=0, column=2)

l2 = tk.Label(root, text="LAST NAME")
l2.grid(row=1)
t2 = tk.Entry(root)
t2.grid(row=1, column=1)
h2 = tk.Label(root, text="(max 30 characters a-z and A-Z)")
h2.grid(row=1, column=2)

l3 = tk.Label(root, text="DATE OF BIRTH")
l3.grid(row=2)
day = StringVar(root)
day.set("Day")
d3d = OptionMenu(root, day, *days)
d3d.grid(row=2, column=1)
month = StringVar(root)
month.set("Month")
d3m = OptionMenu(root, month, *months)
d3m.grid(row=2, column=2)
year = StringVar(root)
year.set("Year")
d3y = OptionMenu(root, year, *years)
d3y.grid(row=2, column=3)


l4 = tk.Label(root, text="EMAIL ID")
l4.grid(row=3)
t4 = tk.Entry(root)
t4.grid(row=3, column=1)

l5 = tk.Label(root, text="MOBILE NUMBER")
l5.grid(row=4)
t5 = tk.Entry(root)
t5.grid(row=4, column=1)

l6 = tk.Label(root, text="GENDER")
l6.grid(row=5)
t61var = StringVar()
t61var.set(0)
t61 = tk.Radiobutton(root, text="MALE", variable=t61var, value=0)
t61.grid(row=5, column=1)
t62var = StringVar()
t62var.set(0)
t62 = tk.Radiobutton(root, text="FEMALE", variable=t61var, value=1)
t62.grid(row=5, column=2)

l7 = tk.Label(root, text="ADDRESS")
l7.grid(row=6)
t7 = tk.Text(root, height=3, width=30)
t7.grid(row=6, column=1)

l8 = tk.Label(root, text="CITY")
l8.grid(row=7)
t8 = tk.Entry(root)
t8.grid(row=7, column=1)

l9 = tk.Label(root, text="PIN CODE")
l9.grid(row=8)
t9 = tk.Entry(root)
t9.grid(row=8, column=1)

l10 = tk.Label(root, text="STATE")
l10.grid(row=9)
t10 = tk.Entry(root)
t10.grid(row=9, column=1)

l11 = tk.Label(root, text="COUNTRY")
l11.grid(row=9)
t11 = tk.Entry(root)
t11.grid(row=9, column=1)

l12 = tk.Label(root, text="HOBBIES")
l12.grid(row=10)
cb121var = IntVar()
cb121var.set(0)
cb121 = tk.Checkbutton(root, text="Drawing",
                       variable=cb121var, onvalue=1, offvalue=0)
cb121.grid(row=10, column=1)

cb122var = IntVar()
cb122var.set(0)
cb122 = tk.Checkbutton(root, text="Singing",
                       variable=cb122var, onvalue=1, offvalue=0)
cb122.grid(row=10, column=2)

cb123var = IntVar()
cb123var.set(0)
cb123 = tk.Checkbutton(root, text="Dancing",
                       variable=cb123var, onvalue=1, offvalue=0)
cb123.grid(row=10, column=3)

cb123var = IntVar()
cb123var.set(0)
cb123 = tk.Checkbutton(root, text="Sketching",
                       variable=cb123var, onvalue=1, offvalue=0)
cb123.grid(row=10, column=4)

cb124var = IntVar()
cb124var.set(0)
cb124 = tk.Checkbutton(root, text="Others",
                       variable=cb124var, onvalue=1, offvalue=0)
cb124.grid(row=11, column=1)

t12 = tk.Entry(root)
t12.grid(row=11, column=2)


l13 = tk.Label(root, text="QUALIFICATION")
l13.grid(row=12)
l131h1 = tk.Label(root, text="Sl.No")
l131h1.grid(row=12, column=1)
l131h2 = tk.Label(root, text="Examination")
l131h2.grid(row=12, column=2)
l131h3 = tk.Label(root, text="Board")
l131h3.grid(row=12, column=3)
l131h4 = tk.Label(root, text="Percentage")
l131h4.grid(row=12, column=4)
l131h5 = tk.Label(root, text="Year of Passing")
l131h5.grid(row=12, column=5)
l132h1 = tk.Label(root, text="1")
l132h1.grid(row=13, column=1)
l132h2 = tk.Label(root, text="Class X")
l132h2.grid(row=13, column=2)
l132h3 = tk.Entry(root)
l132h3.grid(row=13, column=3)
l132h4 = tk.Entry(root)
l132h4.grid(row=13, column=4)
l132h5 = tk.Entry(root)
l132h5.grid(row=13, column=5)
l133h1 = tk.Label(root, text="2")
l133h1.grid(row=14, column=1)
l133h2 = tk.Label(root, text="Class XII")
l133h2.grid(row=14, column=2)
l133h3 = tk.Entry(root)
l133h3.grid(row=14, column=3)
l133h4 = tk.Entry(root)
l133h4.grid(row=14, column=4)
l133h5 = tk.Entry(root)
l133h5.grid(row=14, column=5)
l134h1 = tk.Label(root, text="3")
l134h1.grid(row=15, column=1)
l134h2 = tk.Label(root, text="Graduation")
l134h2.grid(row=15, column=2)
l134h3 = tk.Entry(root)
l134h3.grid(row=15, column=3)
l134h4 = tk.Entry(root)
l134h4.grid(row=15, column=4)
l134h5 = tk.Entry(root)
l134h5.grid(row=15, column=5)
l135h1 = tk.Label(root, text="4")
l135h1.grid(row=16, column=1)
l135h2 = tk.Label(root, text="Masters")
l135h2.grid(row=16, column=2)
l135h3 = tk.Entry(root)
l135h3.grid(row=16, column=3)
l135h4 = tk.Entry(root)
l135h4.grid(row=16, column=4)
l135h5 = tk.Entry(root)
l135h5.grid(row=16, column=5)
l136h1 = tk.Label(root, text="(10 char max)")
l136h1.grid(row=17, column=3)
l136h2 = tk.Label(root, text="(upto 2 decimal)")
l136h2.grid(row=17, column=4)

l14 = tk.Label(root, text="COURSES APPLIED FOR")
l14.grid(row=18)
t141var = StringVar()
t141var.set(0)
t141 = tk.Radiobutton(root, text="BCA", variable=t141var, value=0)
t141.grid(row=18, column=1)
t142 = tk.Radiobutton(root, text="B.Com", variable=t141var, value=1)
t142.grid(row=18, column=2)
t143 = tk.Radiobutton(root, text="B.Sc", variable=t141var, value=2)
t143.grid(row=18, column=3)
t144 = tk.Radiobutton(root, text="B.A", variable=t141var, value=3)
t144.grid(row=18, column=4)

root.mainloop()
