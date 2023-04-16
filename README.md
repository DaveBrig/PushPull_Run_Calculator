# PushPull_Run_Calculator

This Streamlit Application was developed for the Melbourne Strength Culture Push-Pull Run event.  The Application allows a user to calculate the Integrated Balanced Performance (IPB) score which is an aggregation of DOTS score widely used in powerlifting, and a Weight Adjusted Performance (WAP) score developed for comparing One mile running performance across athletes of different gender, age and bodyweight.  WAP is an adaptation of the commonly used Age Graded Performance calculation used to score long distance running events.  

Age Graded Performance (AGP) is calculated using the formula (Record/(Tme x f)) x 100, where Record = 1 Mile Record for the relevant gender (3.47 mins for males and 4.12 mins for females), Time = the 1 mile time, f = Age Grade Factor.  Another use case of this formula can be seen at https://runhive.com/tools/performance-calculator. Age Grade Tables required to calculate this score were obtained from https://github.com/AlanLyttonJones/Age-Grade-Tables.

The formula to obtain Weight Adjusted Performance (WAP) is (bwt/Av_bwt) x AGP, where bwt = athletes bodyweight and Av_bwt = The Average bodyweight of the relevant gender according to the 2018 Australian Bureau of Statistics.  For males this is 87kg and for Females this is 71.8kg.

The DOTS score is calculated by the method outlined in https://www.powerlifting.sport/fileadmin/ipf/data/ipf-formula/Models-Evaluation-I-2020.pdf.

Finally, the IBP is calculated using (DOTS x 0.25) + WAP.  