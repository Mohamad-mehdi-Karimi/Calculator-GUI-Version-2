import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="black")

equation = ""

def show(symbol):
  global equation
  equation += symbol
  label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
       try:
          result = eval(equation)
       except:
          result = "ERROR"
          equation = ""
    label_result.config(text=result)         
            


label_result = Label(root, width=25, height=2, text="", font=("Arial", 30))
label_result.pack()

btn_1 = Button(root, text="C", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear())
btn_1.place(x=10, y=100)
btn_2 = Button(root, text="/", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/"))
btn_2.place(x=150, y=100)
btn_3 = Button(root, text="%", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%"))
btn_3.place(x=290, y=100)
btn_4 = Button(root, text="*", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*"))
btn_4.place(x=430, y=100)

btn_5 = Button(root, text="7", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7"))
btn_5.place(x=10, y=200)
btn_6 = Button(root, text="8", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8"))
btn_6.place(x=150, y=200)
btn_7 = Button(root, text="9", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9"))
btn_7.place(x=290, y=200)
btn_8 = Button(root, text="-", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-"))
btn_8.place(x=430, y=200)

btn_9 = Button(root, text="4", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4"))
btn_9.place(x=10, y=300)
btn_10 = Button(root, text="5", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5"))
btn_10.place(x=150, y=300) 
btn_11 = Button(root, text="6", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6"))
btn_11.place(x=290, y=300)
btn_12 = Button(root, text="+", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+"))
btn_12.place(x=430, y=300)

btn_13 = Button(root, text="1", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1"))
btn_13.place(x=10, y=400)
btn_14 = Button(root, text="2", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2"))
btn_14.place(x=150, y=400)
btn_15 = Button(root, text="3", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3"))
btn_15.place(x=290, y=400)
btn_16 = Button(root, text="0", width=11, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0"))
btn_16.place(x=10, y=500)

btn_17 = Button(root, text=".", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("."))
btn_17.place(x=290, y=500)
btn_18 = Button(root, text="=", width=5, height=3, font=("Arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate())
btn_18.place(x=430, y=400)

root.mainloop()
