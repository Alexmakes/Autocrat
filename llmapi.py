# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI
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



def on_click():
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

def gui():
  root = Tk()
  root.title('Dropdown Menu and Buttons')
  label = Label(root, text="Chose your complaint or press Im feeling unlucky for one to be chosen for you")
  label.pack()

  with open('llmmesseges', 'r') as f:  # replace 'yourfile.txt' with your actual filename
      my_list = [line.strip() for line in f]
  my_listbox = Listbox(root)
  for item in my_list:
      my_listbox.insert(END, item)
  my_listbox.pack()

  go_button = Button(root, text="GO", command=on_click)   # GO button which triggers on_click method when clicked
  go_button.pack()

  random_button = Button(root, text='"Im feeling unlucky"', command=pick_random)  # Random button which adds a random item to the listbox
  random_button.pack()

  cancel_button = Button(root, text='CANCEL', command=on_cancel)   # Cancel button which closes the application
  cancel_button.pack()

  root.mainloop()

gui()
getllmmessege()

