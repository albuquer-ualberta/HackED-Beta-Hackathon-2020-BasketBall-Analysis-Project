import Requests
#from .analysis import threePoint

class player_analysis():
    def __init__(self, name):
        self.szns = [] #list of season analysis
        self.name = name
        self.years_active = []
    
    def szn_count(self, year=2020,typi='all'): #TODO change so multiple analysis modes supported
        while True:
            temp = szn_analysis(year)
            try:
                temp.add_player_structure(self.name,typi=typi)
            except:
                break
            print('as')
            self.years_active.append(year)
            year -= 1
            self.szns.append(temp)
            

class szn_analysis():
    def __init__(self, year):
        self.structures = []
        self.year = year
        self.nba_request = Requests.nba_request()
    
    def add_player_structure(self, name, typi='all'):
        intermediary = []
        if type(typi) == type('string'):
            for x in range(0,5):
                stat = self.add_frame(typi=x)
                full_set = self.create_structure(stat)
                intermediary.append(full_set['STATS'])
                intermediary.append(full_set[name])
                self.structures.append(intermediary)
        else:
            stat = self.add_frame(typi=typi)
            full_set = self.create_structure(stat)
            intermediary.append(full_set['STATS'])
            intermediary.append(full_set[name])
            self.structures.append(intermediary)


    def create_structure(self, frame):
        dic = {}
        dic['STATS'] = list(frame.columns)
        for x in frame.to_numpy():
            if (x[0] != None) and (x[0] not in dic):
                dic[x[0]] = x

        return dic
    
    def add_frame(self, typi=1):
        if typi == 0:
            return self.nba_request.totals(self.nba_request.url, self.year)
        elif typi == 1:
            return self.nba_request.per_game(self.nba_request.url, self.year)
        elif typi == 2:
            return self.nba_request.per_36(self.nba_request.url, self.year)
        elif typi == 3:
            return self.nba_request.per_100(self.nba_request.url, self.year)
        elif typi == 4:
            return self.nba_request.advanced(self.nba_request.url, self.year)
        else:
            print('invalid')


g = player_analysis('Stephen Curry')
print(g.name)
g.szn_count(year=2020, typi=1)
print(g.years_active)
for x in g.szns:
    print(x.structures[0][1])
