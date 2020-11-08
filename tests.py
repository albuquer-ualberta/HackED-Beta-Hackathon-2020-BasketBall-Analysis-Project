import numpy
from basketball_analysis import sznAnalysis

test = sznAnalysis.szn_analysis(2020)

frem = test.add_frame()
struc = test.create_structure(frem)

test.histo_percent(test.szn_dictionaries[0])
print(test.szn_percentile(test.szn_dictionaries[0], metric='FT%'))

stephen = sznAnalysis.player_analysis('Stephen Curry')
stephen.szn_count(year=2020,typi=1)
print(stephen.szns)
print(stephen.years_active)

print(stephen.next_per_game_prediction())

# collective_x = [1,2,3,4,5,6,7,8,9]
# collective_y = [0.437,0.442,0.455,0.453,0.424,0.443,0.454,0.411,0.423]#0.437]

# model = regression(collective_x, collective_y)

# if len(model) == 5:
#     eleven = model[0] * 11 + model[1]
#     print("The year after the last, the 3P% will be:", model(11))

# else:
#     print("The year after the last, the 3P% will be:", model(16))
