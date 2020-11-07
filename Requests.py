import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

class nba_request():
    def __init__(self):
        self.url = 'https://www.basketball-reference.com/leagues/NBA_' # NOT A FULL URL


    def parse_url(self):
        # NBA season we will be analyzing
        year = 2020
        # URL page we will scraping (see image above)

        temp = self.url + "{}_per_game.html".format(year)
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
        print(stats.head(10))


g = nba_request()
g.parse_url()


