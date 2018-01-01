import requests

import pyarks.utility
from pyarks.parkBase import Park
from pyarks.rideBase import Ride


class UniversalJapanPark(Park):
    def __init__(self, name):
        self.rides = self.getRides()
        super(UniversalJapanPark, self).__init__(name)

    def getRides(self):
        rides = []
        response = self.getResponse()
        if response["status"] == 2:
            self.isOpen = False
            return rides
        else:
            self.isOpen = True
            #Fill in here when the park is open
            for waitTimeGroup in response["list"]:
                if utility.USJTranslate(waitTimeGroup["wait"].encode("utf-8")) == "Inactive":
                    waitTime = -2
                else:
                    waitTime = int(waitTimeGroup["wait"][:-1])
                for ride in waitTimeGroup["rows"]:
                    rides.append(Ride(self, utility.USJTranslate(ride["text"].encode("utf-8")), waitTime, ""))
            return rides

    def getResponse(self):
        return requests.get("http://ar02.biglobe.ne.jp/app/waittime/waittime.json").json()
