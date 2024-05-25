# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI
#from tkinter import *
#import tkinter.messagebox as messagebox
import keyboard
import random
#from ttgLib.TextToGcode import ttg
import numpy as np
from handwriting_synthesis.hand import Hand
from pyaxidraw import axidraw 
import readchar


# declaring varibles 

#llmpreprompt = "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of Stockport and they have not being responding to your letter and this is your final straw and tell them how you really feel."
#llmmessege_f = "in the format of Haiku i would like to you to write a complaint about "
llmmessege_f = "in the format of a short poem i would like to you to write a complaint about "
#llmmessege_f = "in the format of a short poem i would like to you to write a complaint about why i can not get a refund on my train ticket and how unfair it is for you too refuse to give me back my money for a unused train ticket "


def getLLMPrePrompt(): # a function that returns the pre prompt so its esay to edit if it needs refining
  #return "In a single short paragraph. you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of "+random_item_from_array(read_file("llmapi/councils"))+" and they have not being responding to your letter and this is your final straw and tell them how you really feel."
  return "you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining to the local council of "+random_item_from_array(read_file("llmapi/councils"))+" and they have not being responding to your letter and this is your final straw and tell them how you really feel." # edit it in to compain about the cointcel 
  #return "you are British and grumpy a petty person of no worth and you can only respond in passive being aggressive statements your life goal is to is too be petty over small civil matters. You find pleasure in complaining " # edit this in to make it not compain about the counticel 

def getLLMPrompt(): # same as pre promt but for the promt this also reads the file and choses a random compaint
  return llmmessege_f+random_item_from_array(read_file("llmapi/llmmesseges")) # edit this in for use at EMF
  #return llmmessege_f # edit this in for use of custom messeges

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
    front=open("llmapi/frontmatter","r")
    #back=read_file("bottommatter")
    back=open("llmapi/bottommatter","r")
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


def split_string(text, chunk_size=73):
    words = text.split()
    chunks = []
    current_chunk = ""
    
    for word in words:
        if len(current_chunk) + len(word) <= chunk_size:
            if current_chunk:
                current_chunk += " " + word
            else:
                current_chunk += word
        else:
            chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks


# this function replaces the first section of the svg its dirty and hacky but works i tried edditing the xml nativly and it was not having it this will work eatch time as the rrm that genrates the hand writing doesnt change this section of the svg. im sorry but it works
def find_replace_with_file_content(source_file_path, replacement_file_path):
    # Read the content of the source file
    with open(source_file_path, 'r') as source_file:
        source_content = source_file.read()

    # Read the content of the replacement file
    with open(replacement_file_path, 'r') as replacement_file:
        replacement_content = replacement_file.read()

    # Find the start and end indices of the substring to be replaced
    start_index = source_content.find('<svg baseProfile')
    end_index = source_content.find('y="0" />', start_index) + len('y="0" />')

    # Replace the substring with the content from the replacement file
    modified_content = source_content[:start_index] + replacement_content + source_content[end_index:]

    # Write the modified content back to the source file
    with open(source_file_path, 'w') as source_file:
        source_file.write(modified_content)



#key = readchar.readkey()
# pressed the go button ( it sends a 1 key stroke )
#while True:
  #key = readchar.readkey()
  #if key == "1":
      #key = 0
      #if keyboard.wait('1') == '1':
      #print("You pressed the 1 key")

print('You Pressed the correct Key!')

preprompt = getLLMPrePrompt()  # Get the pre prompt
prompt = getLLMPrompt()  # Get the prompt

#getllmmessege(getLLMPrePrompt(),getLLMPrompt()) # passes the funcitions to the openai libary to genrate the messege
completion_message = getllmmessege(getLLMPrePrompt(),getLLMPrompt()) # passes the funcitions to the openai libary to genrate the messege


#print(type(completion_message))

#markdown_content = convert_to_markdown(completion_message.content) #.content is the messege in

#save_to_markdown_file(markdown_content, "llmapi_output/output.md") # no longer is used



# prints the output of the LLM formated nicly
print(completion_message.content)
#chat gpt genrated code for the next 3 lines
result = split_string(completion_message.content)
lines = []
for chunk in result: # for loop to append the chuck to the last one with a max of 70 char
  print(chunk)
# start the handwriting demo code
#lines = [completion_message.content]
  lines.append(chunk+"")
#lines = ["this is a test"]
""""
biases = [.75 for _ in lines]
styles = [9 for _ in lines]
stroke_colors = ['red', 'green', 'black', 'blue']
stroke_widths = [1, 2, 1, 2]

hand = Hand()
hand.write(
    filename='img/llmtest1.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
"""
# settings for RRN modle
#fixed bias, varying style
#lines = downtown.split("\n")
biases = [.75 for i in lines]
styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)
stroke_colors = ['red' for i in lines ]
hand = Hand()
hand.write(
    filename='img/llmtest1.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
)

# start the plot
exec(open("plot.py").read())

#gcode = ttg("Text to Gcode",1,0,"return",1).toGcode("M02 S500","M05 S0","G0","G1")
#print(gcode)
#time to use the os function too convert the
#os.system('pandoc output.md -o test.pdf')
#Penplot( getllmmessege(llmmessege,getLLMPrePrompt()))
#key = 0
"""
  #if key == "2":
      key = 0
      #elif keyboard.wait('2') == '2':
      print("You pressed the 2 key")

      ad = axidraw.AxiDraw()
      ad.interactive()
      ad.connect()
      ad.penup()                    # raise pen
      ad.goto(0,0)
      ad.disconnect()
      key = 0
"""
# This keeps the script running and stops it 
  #keyboard.wait('esc')

# input mode for debugging 

#print(random_item_from_array(read_file("llmmesseges")))
#print(read_file("llmmesseges"))
#gui()

#getllmmessege()
