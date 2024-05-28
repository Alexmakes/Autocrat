# AutoCrat
 A machine which write poems in the form of formal complaints to a fictional place that is a generated though a local LLM. The poems will be written with a fountain ben by a pen plotter. The poems will be then handed out to the public to keep.

## build journal

full build [here](http://[alex](http://alexmakes.net/projects/autocrat.html))

## how this works 

A local Large Language Model (LLM) called TheBloke Dolphin 2.1 'Mistral' 7B Q6_K hosted within LLM Studio using its OpenAI API Python interface to pass an API call to the LLM to generate responses for my code in llmapi.py.

Once the user presses the button 'Q' on the keyboard, the code generates a prompt based on a list of known prompts in the file 'llmapi/llm_messages'. Then, it randomly chooses a local authority within the file 'llmapi/councils', passes the pre-prompt and prompt to the LLM, and awaits the response.


Then the response is passed too the handwriting_synthesis [https://github.com/otuva/handwriting-synthesis](https://github.com/otuva/handwriting-synthesis) and that generates a tool path that is cleaned up in plot.py then is sent to the pen plotter plots on to paper via the axidraw api

![](attachments/Pasted%20image%2020240401221055.png)
final result 
![](attachments/Pasted%20image%2020240401221133.png)
 it pen plotting 
