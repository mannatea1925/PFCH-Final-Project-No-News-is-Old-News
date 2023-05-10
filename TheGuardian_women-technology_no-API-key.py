import requests
import json
import time

# do the inital request
base_url = "https://content.guardianapis.com/search"
payload = {
    'api-key': '',
    'q': 'women AND technology',   
    'from-date' : '2022-03-28',
    'to-date' : '2022-04-28',
    'show-fields' : 'headline',
    'page-size': '50',
    'page':1
}

save_data = []
just_911_data = []

r = requests.get (base_url, params=payload)
data = json.loads(r.text)

# loop through that many times, it's not inclusive so we add +1 to the end
for page in range(1,data['response']['pages'] + 1):

    print('Doing page',page)

    # do the request for each page
    payload = {
        'api-key': ' ',
        'q': 'women AND technology',   
        'from-date' : '2022-03-28',
        'to-date' : '2022-04-28',
        'show-fields' : 'headline',
        'page-size' : '50',
        'page':page
    }

    # add in the results to our results to save_data list
    save_data = save_data + data['response']['results']

    # sleep 5 sec so we don't do too many requests at once
    time.sleep(5)

# this is printing just the headlines with '9/11' in it from the date range specified    
print("Total pages:", data['response']['pages'])

with open ('women-technology.json', 'w') as out:
    json.dump(save_data, out, indent = 2)

# count the number of instances    
count = len(save_data)
print(count)

