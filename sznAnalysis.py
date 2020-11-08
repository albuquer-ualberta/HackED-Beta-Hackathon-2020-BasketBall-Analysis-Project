import Requests
#from .analysis import threePoint

class szn_analysis():
    def __init__(self, frame):
        self.frame = frame


    def create_stucture(self, frame):
        dic = {}
        dic['STATS'] = list(frame.columns)
        for x in frame.to_numpy():
            if (x[0] != None) and (x[0] not in dic):
                dic[x[0]] = x

        return dic

g = Requests.nba_request()
table = g.totals(g.url,2020)

#wah = g.adjusted_shooting(g.url, 2019)
testido = szn_analysis(table)
print(testido.create_stucture(table)['Trevor Ariza'])
