import json
import requests
import os
from tqdm import tqdm
from time import sleep

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# create query
query = input('Enter your keyword here: ')
endpage = int(input('How many pages do you want to scrape: '))

# create output folder
cur_dir = os.getcwd()
output = cur_dir + f'/{query}'

if not os.path.exists(output):
    os.mkdir(output)

api_url = ['https://unsplash.com/napi/search/photos?query={}&per_page=20&page={}&xp='.format(query, x) for x in range(1, endpage)]
for url in tqdm(api_url):
    # sent request to the server
    r = requests.get(url, headers=headers)
    json_data = r.json()
    for image in tqdm(json_data['results']):
        image_title = image['alt_description']
        image_url = image['urls']['raw']
        # write image files
        try:
            with open(output + '/' + image_title + '.jpg', 'wb') as file:
                r = requests.get(image_url, stream=True)
                file.write(r.content)
        except:
            pass
    sleep(1)