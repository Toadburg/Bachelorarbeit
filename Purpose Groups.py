import csv
import json
import math
from sqlalchemy import create_engine
import pandas



engine = create_engine('postgresql://postgres:banana@localhost:5432/bachelor')

query = """
SELECT 
    "SERIAL",
    "EPNUM",
    "CLOCKST",
    "MAIN"
FROM timeuse
WHERE "COUNTRY" = 'FI'
"""

df = pandas.read_sql_query(query, engine)
with open('ActivityCodes.json') as json_file:
    codes = json.load(json_file)

df_grouped = df.groupby('SERIAL').agg({
    'EPNUM': list,    # EPNUM zusammenfassen als Liste
    'CLOCKST': list,  # CLOCKST zusammenfassen als Liste
    'MAIN': list      # MAIN zusammenfassen als Liste
}).reset_index()

travel_list = [11,63,64,65,66,67]
purpose_dict = {}
purpose_list = []


for index, row in df_grouped.iterrows():
    for main in row["MAIN"]:
        if main == 68:
            purpose_list.append("Other Travel/ " + codes[str(main+1)])
            print(codes[str(main+1)])
        elif main in travel_list:
            purpose_list.append(codes[str(main)])
            print(codes[str(main)])
    if purpose_list:
        purpose_dict[row["SERIAL"]] = purpose_list
        purpose_list = []


with open('PurposeGroup/FI_purpose_groups.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(purpose_dict.items())