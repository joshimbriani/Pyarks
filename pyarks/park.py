class Park(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.encode("utf-8")

    def updateRideWaitTimes(self):
        print("This method should never be called. It serves as a base for park instances to override")
        return []

    def updateShowTimes(self):
        print("This method should never be called. It serves as a base for park instances to override")
        return []

    def updateOpeningTimes(self):
        print("This method should never be called. It serves as a base for park instances to override")
        return []