import streamlit as st
import pandas as pd
import numpy as np

header = st.container()
dataset = st.container()
WAP = st.container()
DOTS = st.container()
IBP = st.container()


# Add a sidebar 
st.sidebar.subheader("Variables")

# Select Gender
with st.sidebar:
    Gender = st.radio(
        "Select Gender",
        ("Male", "Female"))

# Set Age
with st.sidebar:
   Age = st.select_slider(
    'Set Age', value = 20,
    options=list(range(5,100)))

# Set Bodyweight   
# Set Running Time   
with st.sidebar:
   bwt = st.number_input(label="Bodyweight (kg)",step=1.,format="%.2f", value = 75.0)

# Set Running Time   
with st.sidebar:
   Time = st.number_input(label="One Mile Time",step=1.,format="%.2f", value = 8.00)

# Set Lifting Total   
with st.sidebar:
   Lift_total = st.select_slider(
    'Set Push Pull Total', value = 150,
    options=list(range(40, 600)))
   
global tables

with header:
    st.title('Integrated Performance Score')
    st.text('This application calculates the integrated DOTS and Running Performance Score')

with dataset:
    st.header('Tables') 
    st.text('Loaded Lytton 2020 Age Factors')
    tables = pd.read_csv('AlanLytton_2020.csv')

with WAP:
    st.header('Calculate the Weight Adjusted Performance Score (WAP)')

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
    
    # Get factor
    def get_factor(Age, Gender):
        factor = tables[tables["Age"] == Age]
        factor = factor[Gender]
        factor = factor.iloc[0]

        return(factor)
    
    # Get Age Adjusted Time
    def AAT(Time, f):
        AAT = Time*f

        return(AAT)
    
    # Get Age Graded Performance
    def AGP(Record, adjusted_time):
        AGP = (Record/adjusted_time)*100

        return(AGP)

    A, B, C, D, E, Ideal, Record = gender(Gender)
    f = get_factor(Age, Gender)
    adjusted_time = AAT(Time, f)
    Age_adjusted_performance = AGP(Record, adjusted_time)

    # Define WAP function 
    def WAP(bwt, Ideal, Age_adjusted_performance):
        bwf = bwt/Ideal
        WAP = bwf*Age_adjusted_performance

        return(WAP)

    Weight_Adjusted_Performance = WAP(bwt, Ideal, Age_adjusted_performance)
        
    st.write('WAP Score', Weight_Adjusted_Performance)

with DOTS:
    st.header('Calculate the DOTS Score')

    def DOTS(Lift_total, bwt, A, B, C, D, E):
         
         dots = Lift_total*(500/(A*bwt**4+B*bwt**3+C*bwt**2+D*bwt+E))

         return(dots)

    dots = DOTS(Lift_total, bwt, A, B, C, D, E)
    
    st.write('DOTS Score', dots)

with IBP:
    st.header('Calculate the Integrated Balanced Performance (IBP) Score')

    def IBP(dots, Weight_Adjusted_Performance):
        IBP = (dots*0.25)+ Weight_Adjusted_Performance

        return(IBP)

    score = IBP(dots, Weight_Adjusted_Performance)
    st.write('IBP Score', score)
