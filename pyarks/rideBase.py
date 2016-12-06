class Ride(object):
    def __init__(self, park, name, waitTime, description):
        self.park = park
        self.name = name
        self.waitTime = waitTime
        self.closed = (waitTime < 0 and waitTime > -50)
        self.isQueueable = waitTime > -50
        self.description = description

    def __str__(self):
        return self.name.encode("utf-8")