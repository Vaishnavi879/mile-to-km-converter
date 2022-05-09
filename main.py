from tkinter import *
windows=Tk()
windows.title("Mile to Km converter")
windows.minsize(width=50,height=50)
windows.config(padx=50, pady=50)

def converter():
    mile=float(entry.get())
    km=mile*1.609
    km=round(km,1)
    label4.config(text=km)

#entry
entry=Entry(width=8)
entry.grid(row=0,column=1)

#label
label1=Label(text="is equal to")
label1.grid(row=1,column=0)

label2=Label(text="Mile")
label2.grid(row=0,column=2)

label3=Label(text="Km")
label3.grid(row=1,column=2)

label4=Label(text="0")
label4.grid(row=1,column=1)

#button
button=Button(text="Calculate",command=converter)
button.grid(row=2,column=1)


windows.mainloop()