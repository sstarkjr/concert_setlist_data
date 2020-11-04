import pandas as pd
import numpy as np
import json
import requests
import pprint
import time
import http.client
import mimetypes




#Use Setlist.fm API

exec(open('../../do_not_publish/info.py').read())

conn = http.client.HTTPSConnection("api.setlist.fm")
payload = ''
headers = {
  'Accept': 'application/json',
  'x-api-key': api_key
}

import os
if not os.path.exists('json_responses'):
    os.makedirs('json_responses')


#I want to query 100 pages starting with p=1
for p in range(1,100,1):
    url = ("/rest/1.0/artist/b2e2abfa-fb1e-4be0-b500-56c4584f41cd/setlists?p=" + str(p))
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    
    #break request if status not successful
    if res.status != 200:
        print('bad status at p='+str(p))
        break
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    
    #sleep so I don't violate request limit
    time.sleep(2)
    
    #save json
    #with open(('json_responses/response_'+str(p)+'.json'), 'w') as json_file:
    #    json.dump(data, json_file)


    with open(('json_responses/response_'+str(p)+'.json'), 'w') as json_file:
    	json.dump(data, json_file)

    