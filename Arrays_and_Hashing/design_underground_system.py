class UndergroundSystem:
    def __init__(self):
        self.checkinMap = {} #id->(startstation, starttime)
        self.checkoutMap = {} #(startstation, endstation)->[totaltime, count]


    def checkin(self,id, stationName, t):
        self.checkinMap[id] = (stationName,t)

    def checkout(self,id, endstation, t):
        startstation, time = self.checkinMap[id]
        route = (startstation, endstation)

        if route not in self.checkoutMap:
            self.checkoutMap[route] = [0,0]
        self.checkoutMap[route][0] += t -time
        self.checkoutMap[route][1] += 1


    def getAveragetime(self, startStation, endStation):

        total, count = self.checkoutMap[(startStation, endStation)]

        return total / count


