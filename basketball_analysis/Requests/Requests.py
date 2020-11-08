import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
HackED Beta 2020

This module gets in the data from the URL specified by the user
and returns a final pandas dataframe for further processing
"""

    """ Take in a list of players' names, a wanted parameter and return
    :param a_wanted_parameter: a string defined by the user
    :param full_structure: a dictionary of players' statistics
    :param names: a list of players' names
    :param index_para: index of the wanted parameter depending on the file
    :return:
        a_list_of_wanted_para: a list of wanted parameter for each player
    """


class nba_request():
    def __init__(self):
        self.url = 'https://www.basketball-reference.com/leagues/NBA_' # NOT A FULL URL


    def totals(self, url, year):
        """ This gets the total statistics in a season
    
        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_totals.html', year)
    
    def per_game(self,url, year):
        """ This gets the per-game statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_per_game.html', year)

    def per_36(self, url, year):
        """ This gets the per-36-game statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_per_minute.html', year)
    
    def per_100(self, url, year):
        """ This gets the per-100-game statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_per_poss.html', year)

    def advanced(self, url, year):
        """ This gets the advanced statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_advanced.html', year)

    def play(self, url, year):
        """ This gets the play-by-play statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_play-by-play.html', year)

    def shooting(self, url, year):
        """ This gets the shooting statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_shooting.html', year)

    def adjusted_shooting(self, url, year):
        """ This gets the adjusted shooting statistics in a season

        :param url: an attribute of nba_request object
        :param year: an integer as a season year
        :return:
            df: a data pandas frame
        """
        return self.parse_url(url, '_adj_shooting.html', year)
    

    def parse_url(self, url, extension, year):
        """ Return a panda dataframe based on the extension and season
        
        :param url: (string) an attribute of nba_request object
        :param extension: (string) user specified
        :param year: (integer) user specified
        :return: 
            stats: a pandas dataframe
        """
        # NBA season we will be analyzing
        # URL page we will scraping (see image above)
        merger = "{}" + extension
        temp = url + merger.format(year)
        print(temp)
        # this is the HTML from the given URL
        html = urlopen(temp)
        soup = BeautifulSoup(html, features='lxml')

        # use findALL() to get the column headers
        soup.findAll('tr', limit=2)
        # use getText()to extract the text we need into a list
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
        headers = headers[1:]
        headers


        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

        stats = pd.DataFrame(player_stats, columns = headers)
        return stats

