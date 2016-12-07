from universalJapanBase import UniversalJapanPark
from universalUSBase import UniversalPark

def getPark(name):
    if name == "USF" or name == "IOA" or name == "Universal Studios Florida" or name == "Islands of Adventure":
        return UniversalPark(name)
    elif name == "USJ" or name == "Universal Studios Japan":
        return UniversalJapanPark(name)
    else:
        print "Unsupported park name"
        print "Currently the module supports 'USF' and 'IOA'"
        print "Returning None"
        return None
