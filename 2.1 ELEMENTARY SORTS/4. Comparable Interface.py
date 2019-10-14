class Date:
    month = 0
    day = 0
    year = 0

    def __init__ (self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def compareTo(self, date):
        if self.year < date.year:
            return -1
        if self.year > date.year:
            return +1
        if self.month < date.month:
            return -1
        if self.month > date.month:
            return +1
        if self.day < date.day:
            return -1
        if self.day > date.day:
            return +1
        return 0

if __name__ == '__main__':
    d1 = Date(1, 2, 3)
    d2 = Date(2, 3, 4)
    print(d1.compareTo(d2))