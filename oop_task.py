from tkinter import *
root = Tk()
root.geometry("600x500")
root.title("Sick Class")

Label(root, text="Sickness Code").place(x=40, y=30)
Entry(root).place(x=300, y=30)
Label(root, text="Duration of treatment").place(x=40, y=70)
Entry(root).place(x=300, y=70)
Label(root, text="Doctor's practice number").place(x=40, y=110)
Entry(root).place(x=300, y=110)
Label(root, text="Scan/Consultation fee").place(x=40, y=150)
Entry(root).place(x=300, y=150)




root.mainloop()
