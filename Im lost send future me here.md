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