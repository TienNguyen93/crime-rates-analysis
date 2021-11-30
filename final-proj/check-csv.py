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
Find frequency of admitted times inmateID in df1 
"""
dff = df1.set_index(['INMATEID', 'ADMITTED_DT', 'DISCHARGED_DT'])
dff.sort_index(inplace=True)
dff = dff.reset_index()
print(dff[0:5])

# print(dff.index)


"""
Find how many days btwn AD date & DIS date of a criminal
"""
# Helper function, return the difference between 2 dates
def term(start, end):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    return abs((end - start).days)


# dff['Jail Days Consumed'] = dff.apply(lambda x: term(x['ADMITTED_DT'], x['DISCHARGED_DT']), axis=1)
# print(dff.iloc[0:4])



# for a in admit[1:]:
#     conv = pd.to_datetime(a)
#     diff = conv - pd.to_datetime(dis)
#     print(abs(diff))

# def difference(list1,list2):
#     for a in list1[1:]:
#         conv = pd.to_datetime(a)
#         diff = conv - pd.to_datetime(list2)
#         diff_list.append(diff)
#     return diff_list
#
# diff2 = difference(admit, dis)
# print(diff2)



# dff['Diff'] = (pd.to_datetime(dff['ADMITTED_DT']) - pd.to_datetime(dff['DISCHARGED_DT']).shift(1))
# print(dff[0:5])






"""
Find admitted frequency for each ID
"""
res = dff.groupby('INMATEID').agg(
    Frequency=pd.NamedAgg(column="ADMITTED_DT", aggfunc='count')).reset_index()
# print(res[0:5])

freq = res['Frequency']





"""
Plot??
"""
# sns.barplot(x='ADMITTED_TIMES', y='INMATEID',data=df1)
# plt.show()










# join_1.to_csv("join_2.csv", index=False)