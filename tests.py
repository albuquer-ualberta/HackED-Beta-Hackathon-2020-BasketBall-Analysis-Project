from basketball_analysis import sznAnalysis

# class test_player():
#     def __init__(name):
#         self.name = name
    
#     def full_analysis(year=2020):



test = sznAnalysis.szn_analysis(2020)

frem = test.add_frame()
struc = test.create_structure(frem)

test.histo_percent(test.szn_dictionaries[0])
print(test.szn_percentile(test.szn_dictionaries[0], metric='FT%'))

stephen = sznAnalysis.player_analysis('Stephen Curry')
stephen.szn_count(year=2020,typi=1)

print(stephen.next_per_game_prediction())

