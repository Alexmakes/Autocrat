# Example: reuse your existing OpenAI setup
#import os
#from openai import OpenAI
from tkinter import *
import tkinter.messagebox as messagebox

# declaring varibles

#global my_listbox
llmpreprompt = "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of Stockport and they have not being responding to your letter and this is your final straw and tell them how you really feel."
llmmessege_f = "i would like to you to write a complaint about {}"

llmmessege = ""


def getllmmessege():

  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": llmpreprompt },
      {"role": "user", "content": llmmessege }
    ],
    temperature=0.7,
  )

  print(completion.choices[0].message)


"""
def on_click():
    print(tkvar.get())
    global llmmessege # set global for llmessege
    global llmmessege_f # set global for llmessege_f
    selection = my_listbox.get(my_listbox.curselection())  # gets the current selected item from the listbox
    llmmessege = llmmessege_f.format([selection]) # formats the varible and inserts the user selection from a list
    messagebox.showinfo("Selected", "You have selected: " + str(selection))
    getllmmessege()

def pick_random():
    random_item = random.choice(my_list)
    my_listbox.insert(END, random_item) # adds a new item to the listbox
    messagebox.showinfo("Random Item", "A random line has been added: " + str(random_item))

def on_cancel():
    root.destroy()
"""
root = Tk()
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
prompts=[line.strip() for line in open('llmmesseges', 'r')]

root.title('Dropdown Menu and Buttons')






tkvar = StringVar() #variable that pop up menu uses when item is selected
tkvar.set(prompts[0])

popupMenu = OptionMenu(mainframe, tkvar, *prompts,command=print(tkvar.get())) #drop down menu
Label(mainframe, text="Chose your complaint or press Im feeling unlucky for one to be chosen for you").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
mainframe
go_button = Button(mainframe, text="GO", command=print(tkvar.get()))   # GO button which triggers on_click method when clicked
go_button.grid(row=5,column=1)

  #cancel_button = Button(root, text='CANCEL', command=root.destroy())   # Cancel button which closes the application
  #cancel_button.pack()



print(tkvar.get())
print("testing")
root.mainloop()

#getllmmessege()
