import tkinter as tk
from cal import add,sub,mul,div #importing my other file of calculator
app = tk.Tk()# for main window
app.title("calculator")
app.geometry("300x400")



# Create the entry (input) field for the calculator
entry = tk.Entry(app, font="Arial 20")
entry.pack(pady=10)

def click(event): # function to handle button clicks
    # Get the text of the button that was clicked
    text = event.widget.cget("text")

    if text == "=":
        expression = entry.get() #gets the current input

        try:
            if '+' in expression:
                num1, num2 = expression.split('+')
                result = add(float(num1), float(num2))

            elif '-' in expression:
                num1, num2 = expression.split('-')
                result = sub(float(num1), float(num2))

            elif '*' in expression:
                num1, num2 = expression.split('*')
                result = mul(float(num1), float(num2))

            elif '/' in expression:
                num1, num2 = expression.split('/')
                result = div(float(num1), float(num2))

            else: 
                result = "invalid input"
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)

        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "error")

    elif text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

#create a frame for the entry widget
row1 = tk.Frame(app)
row1.pack()

#now for buttons
bt1 = tk.Button(row1, text = '1', font = 'Arial 18', width = 4, height = 2)
bt1.pack(side = tk.LEFT, padx = 5,pady = 5)
bt1.bind("<Button-1>", click)
#for 2nd
bt2 = tk.Button(row1, text = "2", font = "Arial 18", width = 4, height = 2)
bt2.pack(side = tk.LEFT , padx = 5, pady = 5)
bt2.bind("<Button-1>", click)
#for 3rd
bt3 = tk.Button(row1, text = "3", font = "Arial 18", width = 4, height = 2)
bt3.pack(side = tk.LEFT , padx = 5, pady = 5)
bt3.bind("<Button-1>", click)

btDIV = tk.Button(row1, text = '/', font = 'Arial 18', width = 4, height = 2)
btDIV.pack(side = tk.LEFT, padx = 5, pady = 5)
btDIV.bind("<Button-1>", click)


row2 = tk.Frame(app)
row2.pack()

#for 4th
bt4 = tk.Button(row2, text ='4', font = 'Arial 18', width = 4, height = 2)
bt4.pack(side = tk.LEFT, padx = 5, pady = 5)
bt4.bind("<Button-1>",click)

#for 5th

bt5 = tk.Button(row2, text = '5', font = 'Arial 18', width = 4, height = 2)
bt5.pack(side = tk.LEFT, padx = 5, pady = 5)
bt5.bind("<Button-1>",click)

#for 6th
bt6 = tk.Button(row2, text = '6', font = 'Arial 18', width = 4, height = 2)
bt6.pack(side = tk.LEFT, padx = 5, pady = 5)    
bt6.bind("<Button-1>",click)

btMUL = tk.Button(row2, text = '*', font = 'Arial 18', width = 4, height = 2)
btMUL.pack(side = tk.LEFT, padx = 5, pady = 5)
btMUL.bind("<Button-1>",click)

#for 7th
row3 = tk.Frame(app)
row3.pack()

bt7 = tk.Button(row3, text = '7', font = 'Arial 18', width = 4, height = 2)
bt7.pack(side = tk.LEFT, padx = 5, pady = 5)
bt7.bind("<Button-1>",click)
#for 8th
bt8 = tk.Button(row3, text = '8', font = 'Arial 18', width = 4, height = 2)
bt8.pack(side = tk.LEFT, padx = 5, pady = 5)
bt8.bind("<Button-1>",click)
#for 9th
bt9 = tk.Button(row3, text = '9', font = 'Arial 18', width = 4, height = 2)
bt9.pack(side = tk.LEFT, padx = 5, pady = 5)
bt9.bind("<Button-1>",click)

btSUB = tk.Button(row3, text = '-', font = 'Arial 18', width = 4, height = 2)
btSUB.pack(side = tk.LEFT, padx = 5, pady = 5)
btSUB.bind("<Button-1>",click)


#for 0th
row4 = tk.Frame(app)
row4.pack()

btC = tk.Button(row4, text = 'C' ,font = 'Arial 18', width = 4, height = 2)
btC.pack(side = tk.LEFT, padx = 5, pady = 5)
btC.bind("<Button-1>",click)

bt0 = tk.Button(row4, text = '0', font = 'Arial 18', width = 4, height = 2)
bt0.pack(side = tk.LEFT, padx = 5, pady = 5)
bt0.bind("<Button-1>",click)

btEQ = tk.Button(row4, text = '=', font = 'Arial 18', width = 4, height = 2)
btEQ.pack(side = tk.LEFT, padx = 5, pady = 5)
btEQ.bind("<Button-1>",click)

btnADD = tk.Button(row4, text = '+', font = 'Arial 18', width = 4, height = 2)
btnADD.pack(side = tk.LEFT, padx = 5, pady = 5)
btnADD.bind("<Button-1>",click)
#for subtraction
btnSUB = tk.Button(row4, text = '-', font = 'Arial 18', width = 4, height = 2)
btnSUB.pack(side = tk.LEFT, padx = 5, pady = 5)
btnSUB.bind("<Button-1>",click)


app.mainloop() #stat the app should be in the end of the code