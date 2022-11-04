import csv
import pprint
import pandas as pd
import io

nombre_columnas = ['tw_id', 'fecha', 'n/n','tw_body']

#file_csv = "./dataset_twitter-scraper_2022-04-08_14-13-20-514.csv"

file_csv = "./ayurveda-20221026-142546.csv"

df = pd.read_csv(file_csv, skipinitialspace=True, encoding="utf-8") #usecols=nombre_columnas

#pyfile = io.open(file_csv, mode="r", encoding="utf-8")

df.info()

# Extend view of print
pd.options.display.max_colwidth = 50
print(len(df))
print(df.head())

#df_list = list(df)
#pprint.pprint(df_list)

# df_tw_full_text = df.full_text

# df_tw_full_text.to_csv('tw_full_text.csv', index=False, encoding="utf-8")

#type(df)
#print(df)
#print(pyfile)



# csvreader = csv.reader(file)

#header = []
#header = next(csvreader)
#header

# rows = []
# for row in csvreader:
#         rows.append(row)
# rows