from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x380")
root.title("Sick Class")
root.config(bg="#03045e")

var = StringVar()
cancer = StringVar()
paid = StringVar()

Label(root, text="Sickness Code", font=15, bg="#03045e", foreground="#90e0ef").place(x=40, y=30)
sickcode = Entry(root)
sickcode.place(x=300, y=30)

Label(root, text="Duration of treatment", font=15, bg="#03045e", foreground="#90e0ef").place(x=40, y=70)
duration = Entry(root, width=5)
duration.place(x=300, y=70)

Label(root, text="Weeks/Months", font=15, bg="#03045e", foreground="#90e0ef").place(x=340, y=70)

Label(root, text="Doctor's Practice number", font=15, bg="#03045e", foreground="#90e0ef").place(x=40, y=110)
docprac = Entry(root)
docprac.place(x=300, y=110)

Label(root, text="Scan/Consultation fee", font=15, bg="#03045e", foreground="#90e0ef").place(x=40, y=150)
scan_consult = Entry(root)
scan_consult.place(x=300, y=150)

Label(root, text="Amount paid for Treatment: R", font=15, bg="#03045e", foreground="#90e0ef").place(x=40, y=260)
amount_paid = Label(root, textvariable=paid, font=15,bg="#03045e", foreground="#caf0f8")
amount_paid.place(x=285, y=260)


class Sick():
    def illness(self):
        self.cancerMed = 400
        self.fluMed = 350.50


def illness():
    if var.get() == "Cancer":
        if int(scan_consult.get()) >= 600:
            messagebox.showinfo("Treatment Denied", "Sorry we cannot treat you")
        elif int(scan_consult.get()) < 600:
            paid_result = 400 + int(scan_consult.get())
            paid.set(paid_result)

    if var.get() == "Influenza":
        if int(scan_consult.get()) >= 600:
            flu_result = 350.50 + int(scan_consult.get())
            discount = flu_result - (2/100) * flu_result
            paid.set(discount)

        elif int(scan_consult.get()) < 600:
            flu_result = 350.50 + int(scan_consult.get())
            paid.set(flu_result)


can_btn = Radiobutton(root, cursor="hand2", text="Cancer", font=20, variable=var, value="Cancer", foreground="#caf0f8", bg="#03045e")
can_btn.place(x=40, y=190)

flu_btn = Radiobutton(root, cursor="hand2", text="Influenza", font=20,  variable=var, value="Influenza", foreground="#caf0f8", bg="#03045e")
flu_btn.place(x=40, y=220)

cal_btn = Button(root, cursor="hand2", text="Calculate", command=illness, bg="#0077b6", font=2, foreground="#caf0f8", borderwidth=5, width=20)
cal_btn.place(x=150, y=300)


def clear_all():
    sickcode.delete(0, END)
    duration.delete(0, END)
    docprac.delete(0, END)
    scan_consult.delete(0, END)
    paid.set(" ")


clear_btn = Button(root, text="Clear", command=clear_all,  cursor="hand2", bg="#0077b6", font=2, foreground="#caf0f8", borderwidth=5)
clear_btn.place(x=390, y=250)


def close_app():
    root.destroy()


close_btn = Button(root, text="Close", command=close_app,  cursor="hand2", bg="#0077b6", font=2, foreground="red", borderwidth=5)
close_btn.place(x=390, y=300)



root.mainloop()
