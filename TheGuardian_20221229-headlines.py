import requests
import json

base_url = "https://content.guardianapis.com/search"
payload = {
    'api-key': ' ',
    'date' : '2022-12-29',
    'show-fields' : 'headline'
}
save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)

print (data['response'])
with open ('headlines.json', 'w') as out:
    json.dump(data, out, indent = 2)
    