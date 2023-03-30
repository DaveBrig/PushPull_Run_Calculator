# Import libraries
import pandas as pd
import numpy as np

# Import Age Grading Tables
tables = pd.read_csv('AlanLytton_2020.csv')

"""# Define Variables
Gender = 'Female'
Age = 65
bwt = 60
Time = 10
Lift_total = 200"""

# Define Gender variables:
def gender(gen):
    if 'Male' in gen:
        # Create Mens DOTS Coefficients
        A =  -0.0000010930 
        B = 0.0007391293 
        C = -0.1918759221 
        D = 24.0900756
        E = -307.75076 

        #Physical parameters 
        Ideal = 87
        Record = 3.47

    else: 
        # Create Womens Coefficients
        A = -0.0000010706 
        B = 0.0005158568 
        C = -0.1126655495 
        D = 13.6175032 
        E = -57.96288 

        #Physical parameters 
        Ideal = 71.8
        Record = 4.12

    return(A, B, C, D, E, Ideal, Record)

# Test function
#A, B, C, D, E, Ideal, Record = gender(Gender)
    
# Get factor
def get_factor(Age, Gender):
    factor = tables[tables["Age"] == Age]
    factor = factor[Gender]
    factor = factor.iloc[0]

    return(factor)

# Test Function
#f = get_factor(Age, Gender)

# Get Age Adjusted Time
def AAT(Time, f):
    AAT = Time*f

    return(AAT)

# Test Function
#adjusted_time = AAT(Time, f)

# Get Age Graded Performance
def AGP(Record, adjusted_time):
    AGP = (Record/adjusted_time)*100

    return(AGP)

# Test Function
#Age_adjusted_performance = AGP(Record, adjusted_time)
#print(Age_adjusted_performance)

# Get Weight Adjusted Performance
'''def WAP(bwt, Ideal, Age_adjusted_performance):
    bwf = bwt/Ideal
    WAP = bwf*Age_adjusted_performance

    return(WAP)'''

# Test Function
#Weight_Adjusted_Performance = WAP(bwt, Ideal, Age_adjusted_performance)
#print(Weight_Adjusted_Performance)

# Define DOTS
'''def DOTS(Lift_total, bwt, A, B, C, D, E):

    dots = Lift_total*(500/(A*bwt**4+B*bwt**3+C*bwt**2+D*bwt+E))

    return(dots)'''

#dots = DOTS(Lift_total, bwt, A, B, C, D, E)
#print(dots)

# Define Integrated Balanced Performance
'''def IBP(dots, Weight_Adjusted_Performance):
    IBP = (dots*0.25)+ Weight_Adjusted_Performance

    return(IBP)'''

#score = IBP(dots, Weight_Adjusted_Performance)
#print(score)
