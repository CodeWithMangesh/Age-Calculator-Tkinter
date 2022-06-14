import datetime
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("400x500")
window.title(" Age Calculator App ")
window.config(bg="LavenderBlush4")
name = tk.Label(text="Name :-",bg="LavenderBlush4",fg="lawn green",font="Roman 15 bold")
name.grid(column=2, row=2,padx=10,pady=10)
year = tk.Label(text="Year :-",bg="LavenderBlush4",fg="lawn green",font="Roman 15 bold")
year.grid(column=2, row=4,padx=10,pady=10)
month = tk.Label(text="Month :-",bg="LavenderBlush4",fg="lawn green",font="Roman 15 bold")
month.grid(column=2, row=6,padx=10,pady=10)
date = tk.Label(text="Day :-",bg="LavenderBlush4",fg="lawn green",font="Roman 15 bold")
date.grid(column=2, row=8,padx=10,pady=10)
nameEntry = tk.Entry(fg="black",font="Roman 15 bold")
nameEntry.grid(column=3, row=2,padx=10,pady=10)
yearEntry = tk.Entry(fg="black",font="Roman 15 bold")
yearEntry.grid(column=3, row=4,padx=10,pady=10)
monthEntry = tk.Entry(fg="black",font="Roman 15 bold")
monthEntry.grid(column=3, row=6,padx=10,pady=10)
dateEntry = tk.Entry(fg="black",font="Roman 15 bold")
dateEntry.grid(column=3, row=8,padx=10,pady=10)


def getInput():
    name = nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))

    textArea = tk.Text(master=window, height=4, width=40,font="arial 10 bold",fg="blue",bg="black")
    textArea.grid(column=3, row=14)
    answer = " Heyy {monkey}!!!. You are {age}  old!!! ".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END, answer)


button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink",fg="black",font="Roman 15 bold")
button.grid(column=3,row=12,padx=10,pady=10)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        m = today.month - self.birthdate.month
        d = today.day - self.birthdate.day
        return f"{age} year, {m} months and {abs(d)} days"


image = Image.open('rohit.jpg')
image.thumbnail((200, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=3, row=0)
window.mainloop()
