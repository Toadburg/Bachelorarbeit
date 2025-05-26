import psycopg2
import pandas
from sqlalchemy import create_engine


conn = psycopg2.connect(
    database="bachelor",
    user='postgres',
    password='banana',
    host='localhost',
    port= '5432'
)

conn.autocommit = True
cursor = conn.cursor()

#Nuke table
#cursor.execute('''TRUNCATE "timeUse" CASCADE''')

"""
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "DIARYID"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "VEHICLE"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "COMPUTER"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "AGEKID_HU"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "HEALTH"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "RUSHED"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "ISCO1"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "MIGRANTM"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "REGION_FI"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "REGION_HU"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "REGION"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "PARNTID1"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "PARNTID2"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "PARTID"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "RELREFP"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "OWNHOME"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "CITIZEN"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "EMPSTAT"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "EMPSP"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "SECTOR"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "STUDENT"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "DISAB"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "HLDID"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "URBAN"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "OCCUPO"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "OCOMBWT"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "REGION_ZA"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "CDAY"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "HHTYPE"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "SINGPAR"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "AGEKID"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "AGEKID2"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "COHAB"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "UNEMP"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "MTRAV"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "ALONE"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "ALONE_ALT"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "CHILD"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "SPPART"''')
cursor.execute('''ALTER TABLE "timeuse" DROP COLUMN "OAD"''')
"""


sql = '''SELECT * FROM "timeuse" '''


cursor.execute(sql)
column_names = [desc[0] for desc in cursor.description]
for i in column_names:
    print(i)

for j in column_names:
    #sql2 = '''SELECT * FROM "timeUse" WHERE "column_names[j]" IS NULL '''
    cursor.execute('''SELECT * FROM "timeuse" WHERE NOT("timeuse" IS NOT NULL) ''')
    row = cursor.fetchone()
    if row is not None:
        print(j)
        print(row)



conn.commit()
conn.close()

