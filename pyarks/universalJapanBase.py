import requests

import utility
from parkBase import Park


class UniversalJapanPark(Park):
    def __init__(self, name):
        self.rides = self.getRides()
        super(UniversalJapanPark, self).__init__(name)

    def getRides(self):
        response = self.getResponse()
        if response["status"] == 2:
            self.isOpen = False
            return None
        else:
            self.isOpen = True
            #Fill in here when the park is open
            for waitTime in response["list"]:
                for ride in waitTime["rows"]:
                    print utility.USJTranslate(ride["text"].encode("utf-8"))
            #print response

    def getResponse(self):
        return requests.get("http://ar02.biglobe.ne.jp/app/waittime/waittime.json").json()
