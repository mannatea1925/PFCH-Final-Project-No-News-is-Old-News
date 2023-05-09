import requests
import json
import time


# do the inital request
base_url = "https://content.guardianapis.com/search"
payload = {
    'api-key': ' ',
    'q': '9/11',   
    'from-date' : '2022-09-11',
    'to-date' : '2022-09-18',
    'show-fields' : 'headline',
    'page-size': '50',
    'page':1
}

save_data = []
just_911_data = []

r = requests.get (base_url, params=payload)
data = json.loads(r.text)

# loop through the returned data page by page; its not inclusive so we add +1 to the end
for page in range(1,data['response']['pages'] + 1):

    print('Doing page',page)

    # do the get request for each page
    payload = {
        'api-key': ' ',
        'q': '9/11',
        'from-date' : '2022-09-11', 
        'to-date' : '2022-09-18',
        'show-fields' : 'headline',
        'page-size' : '50',
        'page':page
    }

    for item in data ['response']['results']:
        if '9/11' in item ['fields']['headline']:
            just_911_data.append(item)
            print(item ['fields']['headline'])

    r = requests.get (base_url, params=payload)
    data = json.loads(r.text)

    # add in the results to our results to save_data list
    save_data = save_data + data['response']['results']

    # pause between requests; sleep 5 sec
    time.sleep(5)
    
print("Total pages:", data['response']['pages'])

# write all of the data returned for comparison
with open ('all_headlines.json', 'w') as out:
    json.dump(save_data, out, indent = 2)

# write all of the data with 9/11 in the headline
with open ('911_headlines.json', 'w') as out:
    json.dump(just_911_data, out, indent = 2)

