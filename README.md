# Correlation between Crime Rates and Bail Reform in NYC (2018-2020)

## Overview

**Hypothesis**: Does the 1st Bail Reform increase the crime rate?

**First Bail Reform Key Takeaways**:
- Eliminate many bail & pretrial detention for nearly all misdemeanors and non-violent crimes
- Aims to reduce jail population

**Data**:
- [NYPD Arrests Data (Historic)](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u)
- [2020 population](https://data.cityofnewyork.us/City-Government/2020-population/t8c6-3i7b)
- [Current Estimates of New York City's Population for July 2018](https://www1.nyc.gov/site/planning/planning-level/nyc-population/current-future-populations.page)
- [Crime Rate Formula](https://oag.ca.gov/sites/all/files/agweb/pdfs/cjsc/prof10/formulas.pdf)
- [New York's Bail Reform Law Summary of Major Components](https://www.courtinnovation.org/sites/default/files/media/document/2019/Bail_Reform_NY_Summary.pdf)

**Methods**: Arithmetic calculations, Dataframe manipulations

**Tools**: Pandas, Numpy, Matplotlib

## Techniques
- Filter unnecessary columns by using pd.drop method
- Find the nummber of offenses for 5 boroughs by aggregating the dataframe with groupby method
- Make comparison bar plot & pie charts by using matplotlib


## Main findings
**After the first bail reform on April 1st 2019**:

- Crime rate in the Bronx increases by 5.91%
- Crime rate in the Brooklyn increases by 6.55%
- Crime rate in the Manhattan increases by 6.18%
- Crime rate in the Queens increases by 6.05%
- Crime rate in the Staten Island increases by 0.98%

![image](https://user-images.githubusercontent.com/43976085/179558159-fb9eeba1-4e30-4aed-967c-476517857a91.png)

**Pie charts of crime classifications across the 5 boroughs (2019-2020) shows that**:

- Brooklyn has the highest rate of the felonies classification (49.0%)
- Bronx has the highest rate of the misdemeanors classification (59.9%)

![image](https://user-images.githubusercontent.com/43976085/179559527-f7cbfdca-0604-4abc-a1ef-f4e9fbf1e0f8.png)
![image](https://user-images.githubusercontent.com/43976085/179559552-575deb99-11fa-4e41-bb83-42eb89a360e7.png)
![image](https://user-images.githubusercontent.com/43976085/179559574-4ae6f987-1166-4835-b5e7-e120e6500047.png)
![image](https://user-images.githubusercontent.com/43976085/179559587-975842ca-17c3-4799-a5f6-02fc5de242b3.png)
![image](https://user-images.githubusercontent.com/43976085/179559602-2b6ff70b-71ac-4322-82c5-c4fa873e8d1b.png)


