from hashlib import sha256
import hmac
from datetime import datetime
from base64 import b64encode
import re
import requests
import json

requests.packages.urllib3.disable_warnings()

androidKey = "AndroidMobileApp"
androidSecret = "AndroidMobileAppSecretKey182014"

date = datetime.utcnow().strftime("%A, %d %B %Y %I:%M:%S") + " GMT"
combinedKey = androidKey+ "\n" + date + "\n"
sig = b64encode(hmac.new(androidSecret, combinedKey, sha256).digest()).strip()
sig = re.sub("/\=$/", "\u003d", sig)

parameters = {
		"apiKey": androidKey,
		"signature": sig
		}

headers = {
		"Date": date,
		"Content-Type": "application/json; charset=UTF-8",
		"Accept": "application/json",
		"Accept-Language": "en-us",
		"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.3; en-GB; C6502 Build/10.4.1.B.0.101) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
		}

print sig

r = requests.post('https://services.universalorlando.com/api', headers=headers, data=json.dumps(parameters, ensure_ascii=False), verify=False)


#print r
