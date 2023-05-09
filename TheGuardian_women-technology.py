import requests
import json
import time

# do the inital request
base_url = "https://content.guardianapis.com/search"
payload = {
    'api-key': ' ',
    'q': 'women AND technology',
    'from-date' : '2022-03-28',
    'to-date' : '2023-04-28',
    'show-fields' : 'all',
    'page-size': '50',
    'page':1
}
r = requests.get (base_url, params=payload)
data = json.loads(r.text)

print("Total pages:", data['response']['pages'])

save_data = []

# loop through the returned data page by page; its not inclusive so we add +1 to the end
for page in range(1,data['response']['pages'] + 1):

    print('Doing page',page)

    # do the get request for each page
    payload = {
        'api-key': ' ',
        'q': 'women AND technology',
        'from-date' : '2022-03-28',
        'to-date' : '2023-04-28',
        'show-fields' : 'all',
        'page-size': '50',
        'page':page
    }

    r = requests.get (base_url, params=payload)
    data = json.loads(r.text)

    # add in the results to our results to save_data list
    save_data = save_data + data['response']['results']

    # pause between requests; sleep 5 sec
    time.sleep(5)

with open ('women_technology.json', 'w') as out:
    json.dump(save_data, out, indent = 2)

# count the number of instances    
count = len(save_data)
print(count)
