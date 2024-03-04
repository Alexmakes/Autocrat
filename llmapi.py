# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI
#from tkinter import *
#import tkinter.messagebox as messagebox
import keyboard
import random

# declaring varibles 

llmpreprompt = "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of Stockport and they have not being responding to your letter and this is your final straw and tell them how you really feel."
llmmessege_f = "i would like to you to write a complaint about "

llmmessege = ""



def getllmmessege(prompt,message):

  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": prompt },
      {"role": "user", "content": message }
    ],
    temperature=0.7,
  )

  print(completion.choices[0].message)



def on_click():
    global llmmessege # set global for llmessege
    global llmmessege_f # set global for llmessege_f
    selection = my_listbox.get(my_listbox.curselection())  # gets the current selected item from the listbox
    llmmessege = llmmessege_f.format([selection]) # formats the varible and inserts the user selection from a list
    getllmmessege()

"""
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
"""

def random_item_from_array(array):
    return array[random.randrange(0,len(array),1)]

def read_file(promtfile):
    try:
        with open(promtfile, 'r') as rawfile:
            return sorted([line.strip() for line in rawfile])
    except FileNotFoundError:
        raise Exception("File not found")


while True:  # making a loop
      # used try so that if user pressed other than the given key error will not be shown
        keyboard.wait('q')  # if key 'q' is pressed
        print('You Pressed the correct Key!')
        llmmessege = llmmessege_f+random_item_from_array(read_file("llmmesseges")) # formats the varible and inserts the user selection from a list
        print(llmmessege)
        getllmmessege(llmmessege,llmpreprompt)

        #break  # if user pressed a key other than the given key the loop will break




#print(random_item_from_array(read_file("llmmesseges")))
#print(read_file("llmmesseges"))
#gui()

#getllmmessege()

