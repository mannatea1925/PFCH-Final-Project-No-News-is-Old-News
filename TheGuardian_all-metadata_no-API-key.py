import requests
import json

base_url = "https://content.guardianapis.com/search"
payload = {
    'api-key': ' ',
    'q' : 'michael AND jordan',
    'show-fields' : 'all'
}
save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)

print (data['response'])
with open ('AllMetadata.json', 'w') as out:
    json.dump(data, out, indent = 2)
    