import requests
import json

base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
payload = {
    'api-key': ' ',
    'q': 'michael jordan',
}

save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)

print (data['response'])
with open ('NYtimes_article_metadata.json','w') as out:
    json.dump (data, out, indent=2)
