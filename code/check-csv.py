import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt
import folium

"""
Datasets used:
    *NYPD Arrests Data (Historic)
"""


"""
Columns: 
'INMATEID', 'ADMITTED_DT', 'DISCHARGED_DT', 'RACE', 
'GENDER', 'AGE', 'INMATE_STATUS_CODE', 'TOP_CHARGE'
"""
df1 = pd.read_csv("../dataset/Inmate_Discharges.csv")


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


# dff['Jail Days Consumed'] = dff.apply(lambda x: term(x['ADMITTED_DT'], x['DISCHARGED_DT']), axis=1)
# print(dff.iloc[0:4])
#
# total = dff['Jail Days Consumed'].sum()
# print(total)    #2306650
#
# #Find average of 'Jail Days Consumed'
# avg = dff['Jail Days Consumed'].mean()
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


#--------------------------------------------------------------------------------#
"""
'ARREST_KEY', 'ARREST_DATE', 'PD_CD', 'PD_DESC', 'KY_CD', 'OFNS_DESC',
       'LAW_CODE', 'LAW_CAT_CD', 'ARREST_BORO', 'ARREST_PRECINCT',
       'JURISDICTION_CODE', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'X_COORD_CD',
       'Y_COORD_CD', 'Latitude', 'Longitude', 'Lon_Lat'
"""
df2 = pd.read_csv("../dataset/NYPD_Arrests_Data__Historic_(2019-2020).csv", low_memory=False)
# print(df2[0:5])


"""
Filter out unecessary columns df2
"""
df2 = df2.drop(columns=['PD_CD',
                        'LAW_CODE','KY_CD',
                        'ARREST_PRECINCT', 'JURISDICTION_CODE',
                        'PERP_SEX', 'PERP_RACE'])
print(df2.columns)
"""
Find sum of offense of each boroughs
"""
boro = df2.groupby('ARREST_BORO')['ARREST_KEY'].count()
boro_sum = boro.sum()
# print("BORO1 sum", boro_sum)

bronx_sum = boro[0]
bk_sum = boro[1]
manh_sum = boro[2]
queens_sum = boro[3]
si_sum = boro[4]

"""
Find crime rate of each boro
A crime rate = # of reported crimes(offenses) / total population
the result is multiplied by 100,000
"""
bx_total_pop = 1446788
bk_total_pop = 2648452
manh_total_pop = 1638281
qu_total_pop = 2330295
si_total_pop = 487155

boro_off_sum = [bronx_sum, bk_sum, manh_sum, queens_sum, si_sum]
boro_pop = [bx_total_pop, bk_total_pop, manh_total_pop, qu_total_pop, si_total_pop]

rate = [(x / y) * 100000 for x, y in zip(boro_off_sum, boro_pop)]
rate = np.round(rate)

labels = ('Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island')

#--------------------------------------------------------------------------------#
df3 = pd.read_csv("../dataset/NYPD_Arrests_Data__Historic_(2018-2019).csv", low_memory=False)
print(df2.shape)
"""
Find total crime offenses for each boroughs
"""
boro2 = df3.groupby('ARREST_BORO')['ARREST_KEY'].count()
boro2_sum = boro2.sum()
# print("BORO@ sum", boro2_sum)

bronx_sum2 = boro2[0]
bk_sum2 = boro2[1]
manh_sum2 = boro2[2]
queens_sum2 = boro2[3]
si_sum2 = boro2[4]

"""
Find crime rate of each boro
A crime rate = # of reported crimes(offenses) / total population
the result is multiplied by 100,000
"""
bx_total_pop2 = 1432132
bk_total_pop2 = 2582830
manh_total_pop2 = 1628701
qu_total_pop2 = 2278906
si_total_pop2 = 476179

boro_off_sum2 = [bronx_sum2, bk_sum2, manh_sum2, queens_sum2, si_sum2]
boro_pop2 = [bx_total_pop2, bk_total_pop2, manh_total_pop2, qu_total_pop2, si_total_pop2]

rate2 = [(x / y) * 100000 for x, y in zip(boro_off_sum2, boro_pop2)]
rate2 = np.round(rate2)
# print(rate)

x = np.arange(len(labels))  # the label locations
width = 0.35                # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rate2, width, label='2018-2019')
rects2 = ax.bar(x + width/2, rate, width, label='2019-2020')

# Adjust axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color("#DDDDDD")

# Remove ticks on y-axis
ax.tick_params(bottom=False, left=False)

# Add horizontal grid
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

# Add annotations
for bar in ax.patches:
    ax.annotate(
        format(bar.get_height(), '.0f'),
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha='center', va='center', size=9, xytext=(0,8),
        textcoords='offset points'
    )

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Crime Rate')
ax.set_xlabel('Boroughs')
ax.set_title('Crime Rate per 100,000 general population [2018-2020]' ,
             pad=15, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

# plt.savefig("comp-bar-chart.png")
# plt.show()

# ------------------------------------------------------------------- #
"""
Pie chart of offenses for each boroughs (2019-2020)
"""
# Find the nummber of offenses for 5 boroughs
df_pie = df2.groupby(['ARREST_BORO', 'LAW_CAT_CD'], as_index=False)['ARREST_KEY'].count()

bx_pie = df_pie[df_pie['ARREST_BORO'] == "B"]
bk_pie = df_pie[df_pie['ARREST_BORO'] == "K"]
mh_pie = df_pie[df_pie['ARREST_BORO'] == "M"]
qn_pie = df_pie[df_pie['ARREST_BORO'] == "Q"]
si_pie = df_pie[df_pie['ARREST_BORO'] == "S"]

labels2 = ['Felonies', 'Infractions', 'Misdemeanors', 'Violations']

bx_size = bx_pie["ARREST_KEY"]
bk_size = bk_pie["ARREST_KEY"]
mh_size = mh_pie["ARREST_KEY"]
qn_size = qn_pie["ARREST_KEY"]
si_size = si_pie["ARREST_KEY"]

textprops = {"fontsize":15} # Font size of text in pie chart
colors = ['#ffec00','#ff0000','#007ed6','#52d726']

fig = plt.figure()
ax = plt.subplot()
ax.pie(bx_size, labels=labels2, autopct='%.1f%%',
       textprops =textprops, colors=colors, explode=[0.05]*4)
ax.set_title("Bronx Rate of Offenses [2019-2020]", weight='bold', size=15)
# fig.savefig("bx-pie.png")

fig2 = plt.figure()
ax2 = plt.subplot()
ax2.pie(bk_size, labels=labels2, autopct='%.1f%%',
        textprops =textprops, colors=colors, explode=[0.05]*4)
ax2.set_title("Brooklyn Rate of Offenses [2019-2020]", weight='bold', size=15)
# fig2.savefig("bk-pie.png")

fig3 = plt.figure()
ax3 = plt.subplot()
ax3.pie(mh_size, labels=labels2, autopct='%.1f%%',
        textprops =textprops, colors=colors, explode=[0.05]*4)
ax3.set_title("Manhattan Rate of Offenses [2019-2020]", weight='bold', size=15)
# fig3.savefig("mh-pie.png")

fig4 = plt.figure()
ax4 = plt.subplot()
ax4.pie(qn_size, labels=labels2, autopct='%.1f%%',
        textprops =textprops, colors=colors, explode=[0.05]*4)
ax4.set_title("Queens Rate of Offenses [2019-2020]", weight='bold', size=15)
# fig4.savefig("qn-pie.png")

fig5 = plt.figure()
ax5 = plt.subplot()
ax5.pie(si_size, labels=labels2, autopct='%.1f%%',
        textprops =textprops, colors=colors, explode=[0.05]*4)
ax5.set_title("Staten Island Rate of Offenses [2019-2020]", weight='bold', size=15)
# fig5.savefig("si-pie.png")

# plt.show()

"""
Difference and % increase of crime rate
"""

diff = []
diff_obj = zip(boro_off_sum, boro_off_sum2)
for x, y in diff_obj:
    res = np.round(((x - y) / boro2_sum) * 100, 2)
    diff.append(res)

# print(diff)
#5.91, 6.55, 6.18, 6.05, 0.98



