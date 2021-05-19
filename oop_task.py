from tkinter import *
root = Tk()
root.geometry("600x500")
root.title("Sick Class")

Label(root, text="Sickness Code").place(x=40, y=30)
Entry(root).place(x=300, y=30)
Label(root, text="Duration of treatment").place(x=40, y=70)
Entry(root, width= 5).place(x=300, y=70)
Label(root, text="Weeks/Months").place(x=470, y=70)
Entry(root).place(x=300, y=70)
Label(root, text="Doctor's practice number").place(x=40, y=110)
Entry(root).place(x=300, y=110)
Label(root, text="Scan/Consultation fee").place(x=40, y=150)
Entry(root).place(x=300, y=150)
Radiobutton(root).place(x= 40, y=190)
Label(root, text="Cancer").place(x=65, y=190)
Radiobutton(root).place(x= 40, y=220)
Label(root, text="Influenza").place(x=65, y=220)
Label(root, text="Amount paid for Treatment").place(x=40, y=260)
Label(root, text=" ").place(x=300, y=260)
Button(root, text="Calculate").place(x=40, y=300)
Button(root, text="Clear").place(x=250, y=300)




root.mainloop()
