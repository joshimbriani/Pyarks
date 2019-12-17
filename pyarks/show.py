class Show(object):
    def __init__(self, park, name, showtimes, description):
        self.park = park
        self.name = name
        self.showtimes = showtimes
        self.description = description

    def __str__(self):
        return self.name