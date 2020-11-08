# HackED Beta 2020
# Author: Albert Dinh

import statistics

# Initial parameters
# FIXME Potentially will have to take into account other ways to input
# request_var = Requests.nba_request()
# season = int(input('Enter a season: '))
# req = input('Enter the desired mode: ')

# # FIXME Potentially more modes to add
# if req == 'totals':
#     table = request_var.totals(request_var.url, year=season)
# elif req == 'per-game':
#     table = request_var.per_game(request_var.url, year=season)

# # An object of class
# season_analysis_obj = sznAnalysis.szn_analysis(table)

# # A dictionary of players and their statistics
# structure_obj_szn_analysis = season_analysis_obj.create_stucture(table)

# name_players = list(structure_obj_szn_analysis.keys())[1:]


def get_wanted_parameter(full_structure, names, index_para):
    """ Take in a list of players' names, a wanted parameter and return
    :param a_wanted_parameter: a string defined by the user
    :param full_structure: a dictionary of players' statistics
    :param names: a list of players' names
    :param index_para: index of the wanted parameter depending on the file
    :return:
        a_list_of_wanted_para: a list of wanted parameter for each player
    """
    a_list_of_wanted_para = []
    for name in names:
        stat_for_player = full_structure[name]
        para = stat_for_player[index_para]
        a_list_of_wanted_para.append(para)

    return a_list_of_wanted_para


def compute_median_age(a_para_list):
    """Take in a list and compute the median
    :param a_para_list: a list of parameters for all player
    """
    median_para = statistics.median(a_para_list)

    return median_para


def compute_stdev(a_para_list):
    """ Take in a list and returns its standard deviations
    :param a_para_list: a list of parameters for all player
    :return:
    """
    std_ev = statistics.stdev(a_para_list)


if __name__ == '__main__':
    main()
