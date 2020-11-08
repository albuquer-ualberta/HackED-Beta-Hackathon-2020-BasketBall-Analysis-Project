#HackED Beta 2020
#Author: Neville Albuquerque
import matplotlib.pyplot as plt
import numpy
from scipy import stats
from sklearn.metrics import r2_score

#percentile function that can be used for contextualizing player performance in a season
def n_percentile(collective_scores, metric='3P%', percentile=50): #collective
        percentile = numpy.percentile(collective_scores, percentile) #uses the percentile function from numpy to retrieve 50th percentile
        return percentile #returns the 50th percentile value for analysis 

#histogram function that can be used to see the spread in distribution of various player stats in a season
def histogram(collective_scores): #collective
    plt.hist(collective_scores) #uses the stat values of all players in a season to make a histogram
    plt.show() #displays a histogram
    return

#regression modelling used for machine learning and statistical model based predictions
def regression(collective_x, collective_y): #individual
    slope, intercept, r, p, std_err = stats.linregress(collective_x, collective_y) #tries out a linear regression model
    if abs(r) < 0.6 #if the linear regression's correlation coefficient (measures the associativity of given data) < 0.6 we use polynomial regression
        polymodel = numpy.poly1d(numpy.polyfit(collective_x,collective_y, 3)) #creates a cubic regression model that fits the data better
        return polymodel #returns the cubic model
    else:
        return [slope, intercept, r, p, std_err] #returns the linear regression variables to make a model

#calculates the IQR and removes outliers within the data that could severely hamper statistical analysis
def iqr(ls, years): 
    years_changed = [] #a new list to store the corrected values for x (which is years)
    new_y = [] #a new list having all of the values of y without any outliers or spaces
    q75, q25 = numpy.percentile(ls,[75,25]) #gives us the 75th and 25th percentile which are Quartile 3 and Quartile 1 respectively
    iqr = q75 - q25 #calculates the interquartile range


    for index in range(len(ls)):
        if (ls[index] > q25 - 1.5 * iqr) and (ls[index] < q75 + 1.5 * iqr): #checks whether our data set values are within acceptable ranges
            years_changed.append(years[index]) #accordingly copies the data into years_changed
            new_y.append(ls[index]) #accordingly copies the data into the new updated data list
            
    return new_y, years_changed #returns the two lists


        

