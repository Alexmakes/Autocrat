# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI
#from tkinter import *
#import tkinter.messagebox as messagebox
import keyboard
import random
from ttgLib.TextToGcode import ttg

# declaring varibles 

#llmpreprompt = "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of Stockport and they have not being responding to your letter and this is your final straw and tell them how you really feel."
llmmessege_f = "i would like to you to write a complaint about "


def getLLMPrePrompt(): # a function that returns the pre prompt so its esay to edit if it needs refining
  return "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of "+random_item_from_array(read_file("councils"))+" and they have not being responding to your letter and this is your final straw and tell them how you really feel."

def getLLMPrompt(): # same as pre promt but for the promt this also reads the file and choses a random compaint
  return llmmessege_f+random_item_from_array(read_file("llmmesseges"))

def getllmmessege(preprompt,prompt): # the code for interfacing with open ai it picky about the inputs being strig
  print("PrePrompt:"+preprompt+"\n"+"Prompt:"+prompt) # prints out the pre promp and the promt 
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": preprompt }, # only works if a string
      {"role": "user", "content": prompt } # only works if a string
    ],
    temperature=0.7,
  )

  print(completion.choices[0].message.content)
  return completion.choices[0].message  # Return completion message instead of printing it

def convert_to_markdown(message):
    # Function to convert the completion message to Markdown format
    completed_message = message.replace("\n\n", "\n")
    #completed_message = file.write(read_file("frontmatter")+completed_message+read_file("bottommatter"))
    return f"testing\n{completed_message}\n" 

def save_to_markdown_file(markdown_content, filename):
    # Function to save the Markdown content to a file
    #front=read_file("frontmatter")
    front=open("frontmatter","r")
    #back=read_file("bottommatter")
    back=open("bottommatter","r")
    file=open(filename, "a")
        #file.write(read_file("frontmatter")+markdown_content+read_file("bottommatter")) # reads the front and bottom and cantonate them on to the messege giving the markdown file front matter for style and formating
        #file.write(markdown_content)
    
    # this is a hacky way of doing it but was not working otherwise 
    file.writelines(front)
    file.write("\n")
    file.writelines(markdown_content)
    file.write("\n")
    file.writelines(back)
    file.close()

def random_item_from_array(array): # this function choses a random postion in an array of any lenght
    return array[random.randrange(0,len(array),1)]

def read_file(promtfile): # this function reads the raw file of all the compalints that can be used 
    try:
        with open(promtfile, 'r') as rawfile:
            return sorted([line.strip() for line in rawfile])
    except FileNotFoundError:
        raise Exception("File not found")


while True:  # making a loop
        #keyboard.wait('q')  # if key 'q' is pressed # on the real day un comment this and remove if blar blar
        if input()=="q":
          print('You Pressed the correct Key!')

          preprompt = getLLMPrePrompt()  # Get the pre prompt
          prompt = getLLMPrompt()  # Get the prompt

          #getllmmessege(getLLMPrePrompt(),getLLMPrompt()) # passes the funcitions to the openai libary to genrate the messege
          completion_message = getllmmessege(getLLMPrePrompt(),getLLMPrompt()) # passes the funcitions to the openai libary to genrate the messege
          #print(type(completion_message))
          markdown_content = convert_to_markdown(completion_message.content) #.content is the messege in 
          save_to_markdown_file(markdown_content, "output.md")

          
          #gcode = ttg("Text to Gcode",1,0,"return",1).toGcode("M02 S500","M05 S0","G0","G1")
          #print(gcode)
          #time to use the os function too convert the 
          os.system('pandoc output.md -o test.pdf')
          #Penplot( getllmmessege(llmmessege,getLLMPrePrompt()))




#print(random_item_from_array(read_file("llmmesseges")))
#print(read_file("llmmesseges"))
#gui()

#getllmmessege()
