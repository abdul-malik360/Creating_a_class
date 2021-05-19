from tkinter import *
root = Tk()
root.title("Classes in Tkinter")
root.geometry("500x500")

class Circle:
    myresult = StringVar()
    import math


    def __init__(self, master):
        self.lab1 = Label(master, text="Please enter radius: ")
        self.lab1.place(x=5, y=20)
        self.myentry = Entry(master)
        self.myentry.place(x=150, y=20)
        self.lab2 = Label(master, text=" ", width="50", textvariable=self.myresult)
        self.lab2.place(x=20, y=50)
        self.btn_area = Button(master, text="Calculate Area", command=self.area_of_circle)
        self.btn_area.place(x=350, y=20)


    def area_of_circle(self):
        result = self.math.pi * int(self.myentry.get()) * int(self.myentry.get())
        self.myresult.set(result)



class Rectangle:
    answer = StringVar()



    def __init__(self, master):
        self.instructionl = Label(master, text="Please enter Length: ")
        self.instructionl.place(x=5, y=90)
        self.instructionw = Label(master, text="Please enter Width: ")
        self.instructionw.place(x=5, y=130)
        self.length_entry = Entry(master)
        self.length_entry.place(x=150, y=90)
        self.width_entry = Entry(master)
        self.width_entry.place(x=150, y=130)
        self.ent_result = Label(master, text=" ", width=50, textvariable=self.answer)
        self.ent_result.place(x=20, y=160)
        self.btn_length = Button(master, text="Calculate Area", command=self.area_of_rectangle)
        self.btn_length.place(x=350, y=110)


    def area_of_rectangle(self):
        result = int(self.length_entry.get()) * int(self.width_entry.get())
        self.answer.set(result)



x = Circle(root)
y = Rectangle(root)
root.mainloop()
