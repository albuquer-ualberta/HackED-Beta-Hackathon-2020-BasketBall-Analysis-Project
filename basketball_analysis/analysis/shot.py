import matplotlib.pyplot as plt
import numpy
from scipy import stats
from sklearn.metrics import r2_score


def n_percentile(collective_scores, metric='3P%', percentile=50): #collective
        percentile = numpy.percentile(collective_scores, percentile)
        return percentile

def histogram(collective_scores): #collective
    plt.hist(collective_scores)
    plt.show()
    return

def regression(collective_x, collective_y): #individual
    slope, intercept, r, p, std_err = stats.linregress(collective_x, collective_y)
    if abs(r) < 0.6:
        polymodel = numpy.poly1d(numpy.polyfit(collective_x,collective_y, 3))
        return polymodel
    else:
        return [slope, intercept, r, p, std_err]

def iqr(ls, years):
    years_changed = []
    new_y = []
    q75, q25 = numpy.percentile(ls,[75,25])
    iqr = q75 - q25


    for index in range(len(ls)):
        if (ls[index] > q25 - 1.5 * iqr) and (ls[index] < q75 + 1.5 * iqr):
            years_changed.append(years[index])
            new_y.append(ls[index])
            
    return new_y, years_changed


        
# collective_x = [1,2,3,4,5,6,7,8,9]
# collective_y = [0.437,0.442,0.455,0.453,0.424,0.443,0.454,0.411,0.423]#0.437]

# model = regression(collective_x, collective_y)

# if len(model) == 5:
#     eleven = model[0] * 11 + model[1]
#     print("The year after the last, the 3P% will be:", model(11))

# else:
#     print("The year after the last, the 3P% will be:", model(16))
