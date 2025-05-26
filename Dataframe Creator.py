import pandas as pd
import sqlalchemy as sa
from sqlalchemy.dialects.mssql.information_schema import columns
from tkinter.filedialog import askopenfilename


engine = sa.create_engine('postgresql://postgres:banana@localhost:5432/bachelor')

data_path = askopenfilename()


for df in pd.read_csv(data_path, chunksize=1000):
    df.to_sql('timeuse', engine, index=False, if_exists='append')
    print("Chunk gelesen")


print("Erfolgreich gelesen")








