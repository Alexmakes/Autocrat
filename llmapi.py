# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI
#import tkinter 
#from tkinter import *
#from tkinter import messagebox
#from tkinter import ttk

# declaring varibles 

llmpreprompt = "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of Stockport and they have not being responding to your letter and this is your final straw and tell them how you really feel."
llmpreprompt = "my house is being destroyed for a by pass and i was not told about this"




def getllmmessege():

  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": llmpreprompt },
      {"role": "user", "content": llmpreprompt }
    ],
    temperature=0.7,
  )

  print(completion.choices[0].message)

#def gui():
#  window = Tk()
#  frm = ttk.Frame(window, padding=10)
#  frm.grid()
#  ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#  ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
#  window.mainloop()

  


#gui()
getllmmessege()

