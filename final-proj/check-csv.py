import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Inmate_Discharges.csv
Daily_Inmates_In_Custody.csv
NYPD_Arrest_Data__Year_to_Date_.csv
NYPD_Criminal_Court_Summons_Incident_Level_Data__Year_To_Date_.csv
"""

"""
Columns: 
'INMATEID', 'ADMITTED_DT', 'DISCHARGED_DT', 'RACE', 
'GENDER', 'AGE', 'INMATE_STATUS_CODE', 'TOP_CHARGE'
"""
df1 = pd.read_csv("Inmate_Discharges.csv")



"""
Columns: 
'ARREST_KEY', 'ARREST_DATE', 'PD_CD', 'PD_DESC', 'KY_CD', 'OFNS_DESC',
'LAW_CODE', 'LAW_CAT_CD', 'ARREST_BORO', 'ARREST_PRECINCT',
'JURISDICTION_CODE', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'X_COORD_CD',
'Y_COORD_CD', 'Latitude', 'Longitude', 'New Georeferenced Column'
"""
# df3 = pd.read_csv("NYPD_Arrest_Data__Year_to_Date_.csv")



"""
Columns: 
'SUMMONS_KEY', 'SUMMONS_DATE', 'OFFENSE_DESCRIPTION',
'LAW_SECTION_NUMBER', 'LAW_DESCRIPTION', 'SUMMONS_CATEGORY_TYPE',
'AGE_GROUP', 'SEX', 'RACE', 'JURISDICTION_CODE', 'BORO',
'PRECINCT_OF_OCCUR', 'X_COORDINATE_CD', 'Y_COORDINATE_CD', 'Latitude',
'Longitude', 'New Georeferenced Column'
"""
# df4 = pd.read_csv("NYPD_Criminal_Court_Summons_Incident_Level_Data__Year_To_Date_.csv")


"""
Filter out unecessary columns df1
"""
df1 = df1.drop(columns=['INMATE_STATUS_CODE', 'TOP_CHARGE'])
# print(df1.columns)
# print(df1)


"""
Rearrange df1
"""
dff = df1.set_index(['INMATEID', 'ADMITTED_DT', 'DISCHARGED_DT'])
dff.sort_index(inplace=True)
dff = dff.reset_index()

# print(dff[0:5])
# print(dff.index)


"""
Find *difference btwn AD & DIS dates of a criminal 
     *total
     *average
"""
# Helper function, return the difference between 2 dates
def term(start, end):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    return abs((end - start).days)


dff['Jail Days Consumed'] = dff.apply(lambda x: term(x['ADMITTED_DT'], x['DISCHARGED_DT']), axis=1)
print(dff.iloc[0:4])

total = dff['Jail Days Consumed'].sum()
print(total)    #2306650

#Find average of 'Jail Days Consumed'
avg = dff['Jail Days Consumed'].mean()
# print(avg)    #60.84702841014007




"""
Find frequency of admitted times inmateID in df1 & average
"""
res = dff.groupby('INMATEID').agg(
    Frequency=pd.NamedAgg(column="ADMITTED_DT", aggfunc='count')).reset_index()
# print(res[0:5])

freq = res['Frequency']
# print(freq)

freq = freq.mean()
# print(freq)     #1.3165590053483365



"""
Plot??
"""
# sns.barplot(x='ADMITTED_TIMES', y='INMATEID',data=df1)
# plt.show()



# join_1.to_csv("join_2.csv", index=False)


#