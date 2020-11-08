import numpy

from .Requests import Requests
from .analysis import shot
from .util import util


class player_analysis():
    """
    Create a player analysis object based on a set of season analysis
    :param name: a string of the players name

    """
    def __init__(self, name):
        self.szns = [] #list of season analysis
        self.name = name
        self.years_active = []
        self.reversed = False
        self.next_szn = []
    
    def szn_count(self, year=2020,typi='all'): #TODO change so multiple analysis modes supported
        """ 
        Find all seasons player is active and add to data structure

        :param year: integer defining end year
        :param typi: default string, user program as integer, represents mode of analysis

        :return:
            NONE
            end result is appending singular season to list of seasons
        """
        while True:
            temp = szn_analysis(year)
            try:
                temp.add_player_structure(self.name,typi=typi) #srub previous season for player name
            except:
                break
            
            self.years_active.append(year)
            year -= 1 # decrement years for frames
            self.szns.append(temp)
        return
    
    def reversal(self):
        """ 
        reverse year list and szn list


        :return:
            NONE
            Reverse list depending on if they haven't already been reversed
        """
        if self.reversed is False: #reversal conditional check
            self.szns.reverse()
            self.years_active.reverse()
            self.reversed == True

        return
    
    
    def player_regression(self, index):
        """ 
        Do regression analysis on a singular metric of analysis, ie 3P%

        :param index: integer, 
        :param typi: default string, user program as integer, represents mode of analysis

        :return:
            regresssion model based of the index parameter given(ie 12 for 3P%)
        """
        self.reversal() #make sure reversed
        param_list = []
        amended_year = []
        good_y = []

        for seasons in self.szns:
            param_list.append(float(seasons.structures[0][1][index])) #index through szn list and sub structures,
            # index of particular stat, PER GAME CURRENTLY supported

        good_y, amended_year = shot.iqr(param_list, self.years_active) # apply iqr outlier removal

        return shot.regression(amended_year,good_y)
    
    def next_per_game_prediction(self):
        """ 
        Do regression analysis on a players whole career, predicts next season averages

        :return:
            self.szn specificied data structure of next season that can be added to the total set
        """
        szn_plus = []

        for season in self.szns: # increment through seasons objects

            numerical_flag = False
            for index in range(len(season.structures[0][1])): #STRUCTURES 0 is first in dictionaries list, per game supproted
                success = False
                try:
                    num_temp = float(season.structures[0][1][index]) # try floating index, error for pure string quantities
                    success = True
                except:
                    success = False
                finally:
                    if success:
                        if season.structures[0][0][index] == 'AGE': #AGE check
                            szn_plus.append(int(season.structures[0][1][index]))
                    
                        else:
                            regression_model = self.player_regression(index) #generate regression model for index

                            if type(regression_model) == type(['lst']):  #handle linear vs poly model

                                value = regression_model[0] * (self.years_active[-1] + 1) + regression_model[1]
                                szn_plus.append(round(value,3))
                                numerical_flag = True
                            else:
                                value = regression_model(self.years_active[-1]+1)
                                szn_plus.append(round(value, 3))
                                numerical_flag = True
                                  
                    else:
                        szn_plus.append(season.structures[0][1][index]) # string quantities
                        numerical_flag = False

                        #error handle for polynomial vs linear
                        # add to new array

        szn_plus = szn_plus[0:29] #CASE FOR PER GAME, remove repetition
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
    
    def histo_percent(self, dic set_type='per_game', metric='3P%'): #ANALYSIS OF per game
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
        
        return shot.histogram(percent_list)

    def szn_percentile(self, dic, set_type='per_game', metric='3P%', percentile=50): #ANALYSIS OF per game
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


