# this is an app/FRONT end for the simple ass calculator
import tkinter as tk
import tkinter.messagebox as msg #this is for pop ups and all

from cal import add,sub,mul,div #importing my other file of calculator
app = tk.Tk()# for main window
dark_mode = True # this is for dark mode



colors = {
    "light": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        "btn_bg": "#ffffff",
        "btn_fg": "#000000",
        "entry_bg": "#ffffff",
        "entry_fg": "#000000"},

    "dark": {
        "bg": "#121212",
        "fg": "#ffffff",
        "btn_bg": "#333333",
        "btn_fg": "#ffffff",
        "entry_bg": "white",
        "entry_fg": "white"}
}


app.title("calculator")
app.geometry("300x400")
app.resizable(False, False)  # disables both width and height resizing

def apply_theme(toggle_btn):
    theme = "dark" if dark_mode else "light"
    app.config(bg = colors [theme]["bg"])
    entry.config(bg=colors[theme]["entry_bg"], fg = colors[theme]["entry_fg"])
    for row in [row1, row2, row3, row4]:
        row.config(bg = colors[theme]["bg"])
        for button in [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt0, btnADD, btnSUB, btEQ, btC]:
            button.config(bg = colors[theme]["btn_bg"], fg = colors[theme]["btn_fg"])

    
        

    toggle_btn.config(bg = colors[theme]["btn_bg"], fg = colors[theme]["btn_fg"])


#DARK MODE TOGGLE BUTTON
toggle_row = tk.Frame(app)
toggle_row.pack(pady=10)

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme(toggle_btn)

toggle_btn = tk.Button(toggle_row, text="🌙 Toggle Dark Mode", font="Arial 12", command=toggle_dark_mode)
toggle_btn.pack()







# Create the entry (input) field for the calculator
entry = tk.Entry(app, font="Arial 14")
entry.pack(pady=10)
#type test------------------------------------------
entry.insert(0,"YOU can even type in this")
entry.config(fg = "grey")

#to remove------------------------------------
# idk what the hell this shi is
def on_click(event):
    if entry.get()  == "YOU can even type in this":
        entry.delete(0,tk.END)
        entry.config(fg = "black")

# Remove the placeholder text when a button is clicked  

entry.bind('<FocusIn>', on_click)

def click(event): # function to handle button clicks
    # Get the text of the button that was clicked
    text = event.widget.cget("text")


    if entry.get() == "YOU can even type in this":
        entry.delete(0, tk.END)
        entry.config(fg="black")




    if text == "=":
        expression = entry.get() #gets the current input


        #this is just some easter eggs nthg imp
        if expression == "hello":
            msg.showinfo("yo wassup", "YOU FOUND AN EASTER EGG")
            return
        elif expression == "rickroll":
            msg.showinfo("NEVER GONNA", "GIVE YOU UP...")
            return
        elif expression == "good":
            msg.showinfo("well thats great", "good to know")
            return

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
            msg.showerror("Calculation Error", f"yo dumbass this is still in progress:\n")


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


app.bind("<Return>", click)#this isnt working for now (for enter key bind to "=")






apply_theme(toggle_btn)

app.mainloop() #stat the app should be in the end of the code