import math
import csv
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame
from sqlalchemy import create_engine
import pandas


def get_tagesabschnitt(stunde):
    if 0 <= stunde <= 5:
        return "Nacht"
    elif 6 <= stunde <= 9:
        return "Morgen"
    elif 10 <= stunde <= 11:
        return "Vormittag"
    elif 12 <= stunde <= 13:
        return "Mittag"
    elif 14 <= stunde <= 17:
        return "Nachmittag"
    elif 18 <= stunde <= 21:
        return "Abend"
    else:
        return "Nacht"


engine = create_engine('postgresql://postgres:banana@localhost:5432/bachelor')

query = """
SELECT 
    "SERIAL",
    "EPNUM",
    "CLOCKST",
    "MAIN"
FROM timeuse
WHERE "COUNTRY" = 'KR'
"""

df = pandas.read_sql_query(query, engine)

df_grouped = df.groupby('SERIAL').agg({
    'EPNUM': list,    # EPNUM zusammenfassen als Liste
    'CLOCKST': list,  # CLOCKST zusammenfassen als Liste
    'MAIN': list      # MAIN zusammenfassen als Liste
}).reset_index()

#print(df_grouped)
#df_grouped.to_csv('timegrouptest.csv')

travel_list = [11,63,64,65,66,67,68]
travel_dict = {}


time_group = [0 for i in range(24)]


for index, row in df_grouped.iterrows():
    print(row["SERIAL"])
    for epnum in row["EPNUM"]:
        if row["MAIN"][epnum-1] in travel_list:
            print(str(epnum) + " Travel happend at " + str(math.floor(row["CLOCKST"][epnum-1])))
            time_group[math.floor(row["CLOCKST"][epnum-1])] = time_group[math.floor(row["CLOCKST"][epnum-1])]+1
    #print(time_group)
    travel_dict[row["SERIAL"]] = time_group
    print(travel_dict[row["SERIAL"]])
    time_group = [0 for i in range(24)]

temp_dict = travel_dict.copy()
time_groupDict = {}
temp = 0


for key, value in travel_dict.items():
    if len(set(value)) == 1:
        del temp_dict[key]
        #print("kein travel")
        temp += 1

travel_dict = temp_dict.copy()

tageszeiten_dict = {"Morgen" : 0, "Vormittag" : 0, "Mittag" : 0, "Nachmittag" : 0, "Abend" : 0 , "Nacht" : 0}
tageszeiten_dict_copy = tageszeiten_dict.copy()

for key, value in travel_dict.items():
    print(value)
    for stunde, wert in enumerate(value):
        if wert > 0:
            abschnitt = get_tagesabschnitt(stunde)
            tageszeiten_dict_copy[abschnitt] += wert
    group = max(tageszeiten_dict_copy, key=tageszeiten_dict_copy.get)
    time_groupDict[key] = {"schedule": value, "day": tageszeiten_dict_copy, "timegroup": group}
    print(group)
    tageszeiten_dict_copy = tageszeiten_dict.copy()

print(temp)

with open('TimeGroup/KR_timegroups.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(time_groupDict.items())

time_df = pandas.DataFrame.from_dict(time_groupDict, orient='index')
print(time_df)

counts = time_df['timegroup'].value_counts().sort_index()

bars = counts.plot(kind='bar', color='skyblue', ylim=(0, max(counts)*1.1))
bars.set_yticks(np.arange(0,max(counts)*1.1,500))
plt.xlabel('Time group')
plt.ylabel('Count')
plt.title('Value Counts of Time Group South Korea')

plt.show()