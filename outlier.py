import numpy
from basketball_analysis import sznAnalysis
[2020, 2019, 2018, 2017, 2016]
[400, 420, 423, 21, 430, 398]

# IF linear regression use zscore
# if poly use iqr

test = sznAnalysis.szn_analysis(2020)

frem = test.add_frame()
struc = test.create_structure(frem)

test.histo_3percent(test.szn_dictionaries[0])

stephen = sznAnalysis.player_analysis('Stephen Curry')
stephen.szn_count(year=2018,typi=1)
print(stephen.szns)
print(stephen.years_active)
polynom = stephen.player_regression(12)
print(polynom)
print(polynom(2019))