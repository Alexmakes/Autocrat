# AutoCrat
 A machine which write poems in the form of formal complaints to a fictional place that is a generated though a local LLM. The poems will be written with a fountain ben by a pen plotter. The poems will be then handed out to the public to keep.



## how this works 

A local LLM called TheBloke dolfin 2.1 mistral  7B Q6_K hosted within LLM studio using its OpenAi Api python interface too pass API called too the LLM too generate responses for my code 

in llmapi.py once the user presses the button Q on the keyboard the code generates a prompt based on a list of known prompts in the file 'llmapi/llmmesseges' then randomly choses a local authority within the file 'llmapi/councils' then passes the prepromt and prompt too the LLM and awaits the response 

 then the response is passed too the handwriting_synthesis https://github.com/otuva/handwriting-synthesis and that generates a tool path that is cleaned up in plot.py then is sent to the pen plotter plots on to paper via the axidraw api

![](attachments/Pasted%20image%2020240401221055.png)
final result 
![](attachments/Pasted%20image%2020240401221133.png)
 it pen plotting 
## my project journal 

[Im lost send future me here](Im%20lost%20send%20future%20me%20here.md)
