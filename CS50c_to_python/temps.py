class TestDat:
    
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp
 
    def __repr__(self):
        return self.city + ', ' + str(self.temp) +'\n'
 
if __name__ == '__main__':
 
    Location = [
        TestDat("Austin",97),
             TestDat("Boston",82),
             TestDat("Chicago",85),
             TestDat("Denver",90),
             TestDat("Las Vegas",105),
             TestDat("Los Angeles",82),
             TestDat("Miami",97),
             TestDat("New York",85),
             TestDat("Pheonix",107),
             TestDat("San Francisco",66),
    ]
 
    sortedByTemp = sorted(Location, key=lambda x: x.temp, reverse=True)
 
    print(sortedByTemp)
 