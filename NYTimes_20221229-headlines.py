import requests
import json

base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
payload = {
    'api-key': 'Q8vNzqMpSMsfykSMtm6iRYvTjVzDOaIZ',
    'begin_date': '20221229',
    'end_date': '20221229'
}

save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)

for item in data['response']['docs']:
    print('------')
    if 'headline' in item:
        print (item['headline'])

with open ('NYtimes_12:29:22_headlines.json', 'w') as out:
    json.dump(data, out, indent = 2)
