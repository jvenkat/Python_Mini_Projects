from tkinter import *



MYwindow=Tk()

def convert():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

button1= Button(MYwindow,text="Execute",command=convert)
button1.grid(row=0, column=1)
e1_value=IntVar()
e1=Entry(MYwindow,textvariable=e1_value)
e1.grid(row=0, column=2)
t1=Text(MYwindow,height=1, width=20)
t1.grid(row=0, column=3)
t2=Text(MYwindow,height=1, width=20)
t2.grid(row=1, column=1)
t3=Text(MYwindow,height=1, width=20)
t3.grid(row=1, column=2)
MYwindow.mainloop()
