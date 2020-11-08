import Requests
#from .analysis import threePoint

class player_analysis():
    def __init__(self, name):
        self.szns = [] #list of season analysis
        self.name = name
        self.years_active = []
    
    def szn_count(self, year=2020, typi='per_game'): #TODO change so multiple analysis modes supported
        while True:
            temp = szn_analysis(year)
            try:
                temp.add_player_structure(self.name, typi)

            except:
                break
            self.years_active.append(year)
            year -= 1
            self.szns.append(temp)
            

class szn_analysis():
    def __init__(self, year):
        self.structures = []
        self.year = year
        self.nba_request = Requests.nba_request()
    
    def add_player_structure(self, name, typi='per_game'):
        stat = self.add_frame(typi=typi)
        full_set = self.create_structure(stat)
        self.structures.append(full_set[name])


    def create_structure(self, frame):
        dic = {}
        dic['STATS'] = list(frame.columns)
        for x in frame.to_numpy():
            if (x[0] != None) and (x[0] not in dic):
                dic[x[0]] = x

        return dic
    
    def add_frame(self, typi='per_game'):
        if typi == 'per_game':
            return self.nba_request.per_game(self.nba_request.url, self.year)

# g = szn_analysis(2020)
# print(g.year)
# g.add_player_structure('Steven Adams')
# print(g.structures[0])

g = player_analysis('Steven Adams')
print(g.name)
g.szn_count(year=2020, typi='per_game')
print(g.years_active)
print(g.szns[0].structures[0])
