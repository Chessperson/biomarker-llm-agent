import ollama
import json

data = {"CRYBB2":3.1,"RAF1":0.2,"sphingosine":2.5}
resp = ollama.chat(model='biomarker-agent', messages=[{'role':'user','content':f"Analyze: {data}"}])
print(json.loads(resp['message']['content']))
