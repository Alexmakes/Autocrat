# AutoCrat
A machine which write poems in the form of formal complaints to a fictional place that is a generated though a local LLM. The poems will be written with a fountain ben by a pen plotter. The poems will be then handed out to the public to keep [here](https://alexmakes.net/projects/autocrat.html).

## How this works 

A local Large Language Model (LLM) called TheBloke Dolphin 2.1 'Mistral' 7B Q6_K hosted within LLM Studio using its OpenAI API Python interface to pass an API call to the LLM to generate responses for my code in llmapi.py.

Once the user presses the button 'Q' on the keyboard, the code generates a prompt based on a list of known prompts in the file 'llmapi/llm_messages'. Then, it randomly chooses a local authority within the file 'llmapi/councils', passes the pre-prompt and prompt to the LLM, and awaits the response.


Then the response is passed too the handwriting_synthesis [https://github.com/otuva/handwriting-synthesis](https://github.com/otuva/handwriting-synthesis) and that generates a tool path that is cleaned up in plot.py then is sent to the pen plotter plots on to paper via the axidraw api

<img src="attachments/Pasted%20image%2020240401221055.png" width="600" />

## credit

* Leah from hackspace manchester for help with python
* Henry from hackspace manchester for making the Ai loading screen
* HuggingFace/TheBloke for release of mistral LLM
* Github/otuva for patching handwriting-synthesis to modern tensorflow v2 
* Hackspace Manchester for giving me a place to make this mad project 

# My website

[here](https://alexmakes.net/)
