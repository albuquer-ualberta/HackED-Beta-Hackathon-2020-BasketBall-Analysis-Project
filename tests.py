import numpy
from basketball_analysis import sznAnalysis

test = sznAnalysis.szn_analysis(2020)

frem = test.add_frame()
struc = test.create_structure(frem)

test.histo_percent(test.szn_dictionaries[0])
print(test.szn_percentile(test.szn_dictionaries[0], metric='FT%'))

# stephen = sznAnalysis.player_analysis('Stephen Curry')
# stephen.szn_count(year=2011,typi=1)
# print(stephen.szns)
# print(stephen.years_active)
# polynom = stephen.player_regression(12)
# print(polynom)
# print(polynom(2019))

# print(stephen.next_per_game_prediction())