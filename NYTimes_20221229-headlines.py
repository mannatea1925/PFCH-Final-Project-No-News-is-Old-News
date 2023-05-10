import requests
import json
import time
import math

base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
payload = {
    'api-key': ' ',
    'begin_date': '20221229',
    'end_date': '20221229'
    'page':1
}

save_data=[]

r = requests.get (base_url, params=payload)

data = json.loads(r.text)


# the total number of 'hits' is stored here
hits = data['response']['meta']['hits']

# if 10 hits per page then that means
total_pages = hits / 10

# if there is a remainder then we need to round up
# we can use math.ceil to round up to the nearest whole number
total_pages = math.ceil(total_pages)

print("There are:",total_pages,'total pages')


# # so loop that many times, its not inclusive so we add +1 to the end
for page in range(1,total_pages +1):

    print('Doing page',page)

    payload = {
        'api-key': ' ',
        'begin_date': '20221229',
        'end_date': '20221229',
        'page':page
    }
    r = requests.get (base_url, params=payload)
    data = json.loads(r.text)

    # add in the results to our results to save_data list
    save_data = save_data + data['response']['docs']

    time.sleep(12)

    for item in data['response']['docs']:
        if 'headline' in item:
            print (item['headline'])

with open ('20221229-headlines.json', 'w') as out:
    json.dump(save_data, out, indent = 2)
