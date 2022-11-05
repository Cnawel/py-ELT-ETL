
# importing required libraries
import mysql.connector
import pprint
  
dbConn = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="", database=''
)
print(dbConn)

cursor = dbConn.cursor()


# query = ("SELECT first_name, last_name, hire_date FROM employees "
#          "WHERE hire_date BETWEEN %s AND %s")

query = "SHOW TABLES"

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

#cursor.execute(query, (hire_start, hire_end))

cursor.execute(query)

resultadoQuery = cursor.fetchall()

for x in resultadoQuery:
  pprint.pprint(x)

# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))

cursor.close()

# 0Disconnecting from the server
dbConn.close()