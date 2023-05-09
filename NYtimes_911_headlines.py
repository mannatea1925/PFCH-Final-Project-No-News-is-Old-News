
import requests
import json

base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
payload = {
    'api-key': ' ',
    'q': '9/11',
    'begin_date': '20220911',
    'end_date': '20220918'
}

save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)

for item in data['response']['docs']:
    if 'headline' in item:
        print (item['headline'])

with open ('911_headlines.json','w') as out:
    json.dump (data, out, indent=2)
