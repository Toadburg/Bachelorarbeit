DataCleaning
sql = '''SELECT * FROM "timeUse" '''


cursor.execute(sql)
column_names = [desc[0] for desc in cursor.description]
for i in column_names:
    print("yeah")
for j in column_names:
    #sql2 = '''SELECT * FROM "timeUse" WHERE "column_names[j]" IS NULL '''
    cursor.execute('''SELECT * FROM "timeUse" WHERE NOT("timeUse" IS NOT NULL) ''')
    row = cursor.fetchone()
    if row is not None:
        print(j)
        print(row)

DataframeCreator
#csv_data = pd.read_csv(data_path)

#csv_data.to_sql('timeUse', engine, if_exists='replace')

#df = pd.read_sql("SELECT SERIAL", engine)

#print(df)

# Querying for the list of table names
'''
with engine.connect() as connection:
    tables = connection.execute(sa.text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
    for table in tables:
        print(table[0])
        print("test")
'''
#csv_data['idx'] = csv_data.groupby('SERIAL').cumcount()
#csv_data.set_index(['SERIAL', 'idx'], inplace=True)

#print(csv_data)
#breakpoint()

, ylim=(0, math.ceil(max(counts/100.0))*100)

WHERE "COUNTRY" = 'US'