import psycopg2
import math
import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import numpy as np
#from sklearn.datasets import load_iris
from IPython.display import display


engine = create_engine('postgresql://postgres:banana@localhost:5432/bachelor')

#data = load_iris()

query = """
SELECT "SERIAL", "INCOME"
FROM timeuse
WHERE "COUNTRY" = 'ZA'
"""

df = pandas.read_sql_query(query, engine)
dropped_df = df.drop_duplicates(subset=['SERIAL'], keep='first')

counts = dropped_df['INCOME'].value_counts().sort_index()

print(counts)
print(max(counts)*1.1)

bars = counts.plot(kind='bar', color='skyblue', ylim=(0, max(counts)*1.1), fontsize=18)
bars.set_yticks(np.arange(0,max(counts)*1.1,1000))
plt.xlabel('Income', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.title('Value Counts of Income for South Africa', fontsize=18)




#display(df)

#df.plot(kind="bar", x='AGE', y='AGE')




plt.show()





