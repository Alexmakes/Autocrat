from tkinter import *
import random
ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B90C')

def display_selected(choice):
    choice = variable.get()
    print(choice)

countries = [line.strip() for line in open('llmmesseges', 'r')]

# setting variable for Integers
variable = StringVar()
variable.set(countries[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *countries,
    command=display_selected
)
go_button = Button(ws, text="GO", command=display_selected)   # GO button which triggers on_click method when clicked

# positioning widget
dropdown.pack(expand=True)
go_button.pack
# infinite loop
ws.mainloop()

def pick_random(list):
    temp=[line.strip() for line in open('llmmesseges', 'r')]
    return temp[random(0,temp.length)]
