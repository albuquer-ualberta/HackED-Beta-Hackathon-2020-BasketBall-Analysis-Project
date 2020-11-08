import numpy

from .Requests import Requests
from .analysis import shot
from .util import util


class player_analysis():
    def __init__(self, name):
        self.szns = [] #list of season analysis
        self.name = name
        self.years_active = []
        self.reversed = False
        self.next_szn = []
    
    def szn_count(self, year=2020,typi='all'): #TODO change so multiple analysis modes supported
        while True:
            temp = szn_analysis(year)
            try:
                temp.add_player_structure(self.name,typi=typi)
            except:
                break
            
            self.years_active.append(year)
            year -= 1
            self.szns.append(temp)
    
    def reversal(self):
        if self.reversed is False:
            self.szns.reverse()
            self.years_active.reverse()
            self.reversed == True
    
    
    def player_regression(self, index):
        self.reversal()
        param_list = []
        amended_year = []
        good_y = []
        for seasons in self.szns:
            param_list.append(float(seasons.structures[0][1][index]))

        good_y, amended_year = shot.iqr(param_list, self.years_active)

        return shot.regression(amended_year,good_y)
    
    def next_szn_prediction(self):
        szn_plus = []

        for index in range(len(self.szns[0][0])):
            success = False
            try:
                num_temp = float(self.szns[0][1][index])
                success = True
            except:
                success = False
            finally:
                if success:
                    self.player_regression(index)
                    #error handle for polynomial vs linear
                    # add to new array
                else:
                    #carry value from last season forward
                    #add to new array
        
        #return new array
            


class szn_analysis():
    def __init__(self, year):
        self.structures = []
        self.year = year
        self.nba_request = Requests.nba_request()
        self.szn_dictionaries = []
    
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
        self.szn_dictionaries.append(dic)
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
    
    def histo_3percent(self, dic): #ANALYSIS OF per game
        three_percent_list = []

        for x in dic:
            if dic[x][12] != '' and (dic[x][12] != '3P%'):
                three_percent_list.append(float(dic[x][12]))
        
        return shot.histogram(three_percent_list)

        def szn_50_3percent(self, dic): #ANALYSIS OF per game
            three_percent_list = []

            for x in dic:
                if dic[x][12] != '' and (dic[x][12] != '3P%'):
                    three_percent_list.append(float(dic[x][12]))
            
            return shot.fifty_percentile(three_percent_list)



# g = player_analysis('Stephen Curry')
# print(g.name)
# g.szn_count(year=2020, typi=1)
# print(g.years_active)
# for x in g.szns:
#     print(x.structures[0][1])
