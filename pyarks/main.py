from hashlib import sha256
import hmac
from datetime import datetime
from base64 import b64encode
import re
import requests
import json

requests.packages.urllib3.disable_warnings()

SHARED_HEADERS = {
    'Accept'                          : 'application/json',
    'Accept-Language'                 : 'en-US',
    'X-UNIWebService-AppVersion'      : '1.2.1',
    'X-UNIWebService-Platform'        : 'Android',
    'X-UNIWebService-PlatformVersion' : '4.4.2',
    'X-UNIWebService-Device'          : 'samsung SM-N9005',
    'X-UNIWebService-ServiceVersion'  : '1',
    'User-Agent'                      : 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-N9005 Build/KOT49H)',
    'Connection'                      : 'keep-alive',
    'Accept-Encoding'                 : 'gzip'
  }

androidKey = "AndroidMobileApp"
androidSecret = "AndroidMobileAppSecretKey182014"

date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
combinedKey = androidKey+ "\n" + date + "\n"
sig = b64encode(hmac.new(androidSecret, combinedKey, sha256).digest()).strip()
sig = re.sub("/\=$/", "\u003d", sig)

parameters = {
		"apiKey": androidKey,
		"signature": sig
		}

headers = {
		"Date": date,
		"Content-Type": "application/json; charset=UTF-8"
		}

headers.update(SHARED_HEADERS)

r = requests.post('https://services.universalorlando.com/api', headers=headers, data=json.dumps(parameters, ensure_ascii=False), verify=False)

headers = {
    'X-UNIWebService-ApiKey' : 'AndroidMobileApp',
    'X-UNIWebService-Token' : r.json()['Token'] 
}

headers.update(SHARED_HEADERS)
r = requests.get('https://services.universalorlando.com/api/pointsofinterest/rides?pageSize=all', headers=headers)
results = r.json()['Results']
for item in results:
    #print item["VenueId"]
    if item['VenueId'] == 10010:
        #print item
	    print item['MblDisplayName'], " - ", item['WaitTime']