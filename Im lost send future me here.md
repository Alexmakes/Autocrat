# contact 
email with EMF in proton mail 
hex chat in libra chat for irrc 
# what i have i done 

todo list is found on 2Do !!!

1. using gpt4all i have got running on the dell power edge a LLM that will respond to a user from a promt it doesnt have a means of inputting information into the command at the moment 
2. using a tool chain of windows applications i got a pen plotter to write a messege if manual transferred with a hershies font  the pen plotter best used a ball point the end goal is to use a fountain pen
3. the paper is to be moved around the machine with pvc pipe rollers on scate board bearings mounted to wood so that i can be hacked together on a small buget while making it as simple to build as possible 
	1. the pcb is being made in tinker cad at https://www.tinkercad.com/things/dmjyJZViut4-brilliant-kieran-waasa/editel it uses photo gates to see the paper and a hbridge to control motors with an uno to control it all
	3. the code is ~/Code/photogate
4. the pen plotter needs to be build 
5. folding machine is too be bought from this guy and to be built 

standards being used 

m3 bolts whenever a bolt is needed for anything
m8 smooth rods when ever anything needs to rotate
skateboard bearings used for bearings 
PCV - WIP
3d printed parts out of PLA when possible on a prusa Mk4



# progress report

## merge Ai sections from other documents 

## paper control 21 11 2023

designed this controller for paper control via photo gates and dc motors controlled via bridge see pic 
![](attachments/Pasted%20image%2020231121170711.png)

code for the photo gates is in ~/Code/photogate 
note removed the 12V and the 5V grounds separate 

## circuit board issues 28 11 2023 

h bridges are working now i have worked out you need twise the number of them to control 4 motors and working round a floating ground issue messing with the logic voltage. 
![](attachments/Pasted%20image%2020231128155430.png)
current issue is trying to pull down the voltage on the photogates are not being pulled down and remain at logic level High

replaced the photo transistors for photo resistors as the logic level wasnt low enough
new lay out 
![](attachments/Pasted%20image%2020231128170840.png)


## day at the LIB 14 12 2023

using darw i have started the flow dirgram for the firmware you can find it at ./draw io 
i have added error catching and photogate control to the flow digram and added the input for the user , still dont kow where to use servos or not it depends on wheather the paper comes out stright from the stack and if it needs stopping or not. i have left the flow chart at the the plotter io state image is bellow, still need to add this to hack a day .io
![](attachments/Pasted%20image%2020231214171321.png)

# day at the lib 18 12 2023 
made progreess with the flow chart and made a digram of the machine for the first time in its latest form, notable is the motor that inserts the paper into the plotter never lets go while its been writen on and instead uses a servo to change paths of the paper to a below level where the folding machin is housed
![](attachments/Pasted%20image%2020231218171923.png)

# 22012024 i made it real this time 

using the code from this website https://microcontrollerslab.com/arduino-l293d-motor-driver-shield-tutorial/
and the pic of the test stand

![](attachments/Pasted%20image%2020240122205408.png)

# 23012024 got the motors working 

wrote soem code to get the motors working using deepseek to debug sections. problem with the delay() in the loop stopps anthing below it from working so all delays should be in functions 
got a if statment wootorking that will call the turnonmotor() function if not will turn off the motors with its relvent function 

see me on thursday
todo add in the photo gate circits and code in the if statments 


![](attachments/Pasted%20image%2020240123222952.png)
# 17022024 killed off the paper idea its taking too long
moved over to getting the code working and found that axi draw have an API fro there drawing program https://axidraw.com/doc/cli_api/ and im able to to use it to build it 
got to the install via `python3 -m pip install https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip` it conflicted need to come back later

# 19022024  got axicli to work you can find it here 

`/home/alex/Documents/Autocrat/AxiDraw_API_396/python3 axicli.py --help`

1. first i need to get the ouput of LLM studio
2. first i need to get the ouput of sample of the input of axicli.py
3. first i need to get the ouput of libra office cli for formating 
4. then glue them together
# 20022024 got the dependicies working now lets code like a boss

re installed the openai lib via pip and now using pip3, it now all works 


theier should be a script that the user generates the promt via adlib 
so a box of of a location . 

i have gotton the code to work file name is llmapi.py a

now have the wizardllm uncensored and it works fine i can now genrate the equired text about what ever i like

# 22022024 now what 

tool chain so far 

LLM manger -> Libra office template -> exsport as pdf -> pdf2svg  to svg -> axidraw to gcode

for pdf to svg im going to be using https://github.com/dawbarton/pdf2svg with the tool chain of `pdf2svg <input.pdf> <output.svg> [<page no of pdf or "all">]`

pandoc could also work with `pandoc input.txt -o output.pdf`


minor issues 
1. potholes
2. dirty buss stops
3. cyclists 
4. bin lorry too early
5. un emted bins
6. too much graffiti
7. children having too much fun during shcool hours
8. bus is late
10. people parking outside my house 
11. gum
12. post office closes to early
13. not enough cash machines
14. roads brumby
15. taking too long to complain
16. the bridge is an awful color
17. horrible cycle paths
18. emails with the wrong name on them
19. People who don't indicate 
20. The queue at the coffee shop moves far too slowly.
21. Overcrowded public transport during rush hour.
22. The constant interruption of your favorite TV show by annoying advertisements.
23. Overpriced items in corner shop
24. Inconsiderate dog owners who don't clean up after their 
25. pets.
26. Littering in public places
27. The inefficiency of public transportation systems, with frequent delays and cancellations.
28. Overly enthusiastic salespeople who follow you around the store without giving you space to browse.
29. Long waiting times for appointments at medical facilities, causing unnecessary stress.
30. People who don't put their shopping trollies  in the designated area after use.
31. The lack of accessible public restrooms for individuals with disabilities.
32. Traffic during peak hours, wasting valuable time and increasing road congestion.
33. Unreliable internet connections during important video calls or online gaming sessions.
34. The seemingly endless construction work on major roads.
35. Noisy neighbours who host frequent parties or engage in loud activities late into the night.
36. People who don't flush the toilet in public restrooms, leaving the next user with an unpleasant task.
37. The lack of adequate parking spaces in busy areas, forcing you to walk long distances with your shopping bags or heavy luggage.
38. stale sandwiches
39. Excessively loud televisions in public spaces
40. food waste
41. Overcrowded gyms
42. The decline of traditional letter writing due to the rise of electronic communication, leading to the loss of a cherished form of personal connection.
43. Inconsistent recycling practices
44. the double yellow lines aren't yellow enough 
45. neighbours house house looks too good makes mine look bad 
46. neighbours window sunlight into my eyes at noon
47. neighbours hedge too tall
48. neighbours hedge too short
49. corner shop does stock my favourite biscuits 

# 25022024 adding git and variables 

added it to my git i used deepseek 7b model to help with making the UI as ive not made anything with gui before, after reading the code from the printer in the hackspace i chose too use the same library tkinter. 

# 29022024 it works and its ugly 

did some coding on the way home from the space and bashed out a GUI with the help of deep seek as i not used that library before and it works. 
![](attachments/Pasted%20image%2020240229151606.png)

next task is too get the ui to call the right functions with the data selected by the user 

## designing the machine 
how this machine is going to be layed out with a track ball in the front of the monitor and the pen plotter too the side 



## new desgin a big red button that says compian

the code will use the keyboard lib and a HID device that uses a high funcution key when pressed to send a random compaint from the text file and print that tker is pissing me off


# 04032024 going to be a good day 

possible to use an uno as a HID device and have a microswitch tigger a keyboard button maybe thiers a HackDay article on the subject

todo
1. get the code to trigger text gen on a button press DONE
2. get the promts to read the file of promts randomly and add this to the varible of the prompt DONE
3. get a one button keyboard to work 



## good news 
both my CPP's for EMF camp have been accepted that is both this autocrat and the trebuchet 

## even better news it works 

![](attachments/Pasted%20image%2020240304210653.png)
made the code more functional and less procedural you now can edit the promt and pre promt in thier own functions and are genrated on the fly from a list of promts and councils  

# 11032024 txt to gcode the story

writing more functions 

my code doesnt work i wrote a lot of functions so will come back tomorrow and re do it

# 12032024 get in the .md

wrote more code to get it to output into a .md file however this is all on one line a porblem for later

1. DONE fix output of convert_to_markdown(message): too format using the /n for new lines

now time to get it talking to pandoc its having a hissy fit using this command pandoc -f markdown output.md -t test.pdf

fixed the output of the message and fixed the /n with a replace 

2. encoding error

# 14032024

code works to produce pdf file now need to format the file to look like a letter using LaTex

1. use the built in pyhon read file functiuon to read the file as the front matter is being added to the output.md in one line 
now complaining about font familys like the front mater worked !

# 1803202024

built the pen plotter and got it plotting 

its fowarware is here https://wiki.evilmadscientist.com/AxiDraw


# 19032024 api time and testing time

debugging the pen plotter as their was some issues with voltage on the stepper drivers as so upped them to 0.8v over 0.5v this solved the issue

![](attachments/Pasted%20image%2020240319231441.png)
did some user testing on single line fonts and found a couple contenders one beeing 
* EMSNeato
* EMSDelight 
both can be found in the fonts folder of the repo 

updated the board to work with a the home Gcode now its orgin is in the top left of the machine 

code is being started to be made on the automatic plotting of the markdown with the plot.py file 

added files to make svg and try and convert them this can be found in the history of chatgpt and the ![](attachments/Pasted%20image%2020240319230958.png)
and ![](attachments/Pasted%20image%2020240319231018.png)
files 

### ai hand writing here 
https://github.com/sjvasquez/handwriting-synthesis 
this was used by stuff made here to great affect it should solve both the hand writing issue and taking the text and converting into somthing that the pen plotter can use 

1. get the repo working 
ive added it rep

# 21032024 build tensor flow from source 

https://github.com/sjvasquez/handwriting-synthesis  needs tensor flow and as i dont have a gpu in the server i wil be needing it to be done using cpu so that means building from source YAY/s 

```shell
export CUDA_VISIBLE_DEVICES=""
```

updated the git to this new repo https://github.com/otuva/handwriting-synthesis


## its working 
to get the genration working you need to get it to running in a enviroment 
```shell

(hand_gen_env) alex@henry:~/Documents/Autocrat/handwriting-synthesis$ python3 -m venv hand_gen_env
(hand_gen_env) alex@henry:~/Documents/Autocrat/handwriting-synthesis$ python main.py
```

## struggling to get axidraw  connected to the server 


got the axi draw working on the server i needs a regex from the height="100%" to height="1052.362179" and width="100%"  to width="744.09447"

the pen plotter chrashes now this is good fun/s 

good idea is to try and realses the internal of the pen plotter and try again 

the above code works btw and now need to get it working for my project


# 26032024 nearly their 

things too do 
- [x] regex replace the 100% with a4 dimentions so that i can be pen plotted 
- [x] split up the compaint into 75 char lines 
- make a button and attach it to the plotter
- write a good read me 
- comit new code
- cite who i got this forcked code off 
- [x] line 118 is sus got need to look at that look at chat gpt
- [x] fix the ns0 attribuite in plot.py

things i have done today 
i have managed to get the hand writing recersive modle working and it now is installed into my code with the output of the LLM bing piped into the input of the modle. also i have added a plot.py file for testing the plotter as it was having issues with realibillity, this was solved with re flowing the usb port ont the pcb and changing out the cable


# 29032024 almost 

fixed the code that sorts the lines into 75 char long and now outputs a short poem this is a good idea as its speeds things up 
probblem is that it still draws the box the issue is that the <ns0:defs /><ns0:rect height="1052.362179" width="744.09447" x="0" y="0" /> is making a black sqaure that the plotter plots and its an issue alos having stability issues with the code 
the git has also gone missing so need to repair that
an idea is too whole sale replacemnt of top of the svg and get the correct one from the bottom axi draw api 

# 01042024 its working

used a hacky fix to make sure the svg is valid by chopping off the top and adding valid svg headers from a known file. 
tramed in the plotter as it was having isses with one side being a little too high
code now works after i spent so long trying to get it to work this has taken a long time

so far i have
1. learnt eltronics from scratch only not too use it in the this progect as it would have taken too long
2. though it could be done in a long shell script how wrong i was
3. learnt python3 with the help of the hackspace and my own dedication
4. screamed at a server for far too long
5. knowing how to maintain a ubuntu server and get linux to do things i never thought i could do without re imaging it.
6. building a pen plotter without instrictions as there whernt any
7. interfacing with an api 
8. writing a function for that