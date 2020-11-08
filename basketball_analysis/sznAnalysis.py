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
    
    def next_per_game_prediction(self):
        szn_plus = []
        print(self.szns[1].structures)
        for season in self.szns:
            print(season.structures[0][1][0])
            for index in range(len(season.structures[0][1])): #STRUCTURES 0 is temp
                success = False
                try:
                    num_temp = float(season.structures[0][1][index])
                    success = True
                except:
                    success = False
                finally:
                    if success:
                        if season.structures[0][0][index] == 'AGE':
                            szn_plus.append(int(season.structures[0][1][index]))
                        else:
                            print(season.structures[0][1][index])
                            regression_model = self.player_regression(index)
                            if type(regression_model) == type(['lst']):
                                value = regression_model[0] * (self.years_active[-1] + 1) + regression_model[1]
                                szn_plus.append(round(value,3))
                            else:
                                value = regression_model(years_active[-1]+1)
                                szn_plus.append(round(value, 3))
                        
                    else:
                        szn_plus.append(season.structures[0][1][index])

                        #error handle for polynomial vs linear
                        # add to new array
        temp = [[season.structures[0][0]]]
        temp[0].append(szn_plus)

        return temp
        
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
        """ Take in an integer and return a Pandas dataframe

        :param typi: (integer) user input for the choice of file
        :return:
            a Pandas data frame
        """
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
    
    def histo_percent(self, dic):
        """ Get a histogram
        
        :param dic: (dictionary) statistics of a season
        :return: 
            a histogram from a season's wanted parameter
        """
        three_percent_list = []

        for x in dic:
            if dic[x][12] != '' and (dic[x][12] != '3P%'):
                three_percent_list.append(float(dic[x][12]))
        
        return shot.histogram(three_percent_list)

    def szn_percentile(self, dic, set_type='per_game', metric='3P%', percentile=50): #ANALYSIS OF per game
        """ Return the 50th percentile

        :param dic: (dictionary) statistics for one season
        :param set_type: (string) a type of file
        :param metric: (string) a wanted metric
        :param percentile: (float) the nth percentile
        :return:
        """
        percent_list = []
        index = 12
        if metric == 'FG%':
            index = 9
        elif metric == '3P%':
            index = 12
        elif metric == '2P%':
            index = 15
        elif metric == 'eFG%':
            index = 16
        elif metric == 'FT%':
            index = 19
                
        for x in dic:
            if dic[x][index] != '' and (dic[x][index] != metric):
                percent_list.append(float(dic[x][index]))
            
        return shot.n_percentile(percent_list)


