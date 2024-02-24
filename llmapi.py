# Example: reuse your existing OpenAI setup
import os
from openai import OpenAI

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


getllmmessege()
