import sqlite3

#connect to db
conn = sqlite3.connect('AlarmData.db')

#create cursor
cursor = conn.cursor()

##create table
#cursor.execute("""
#    CREATE TABLE AandT (
#        TagNo TEXT PRIMARY KEY,
#        LL_Trip REAL, 
#        L_Trip REAL,
#        H_Trip REAL, 
#        HH_Trip REAL,
#        ALMPR INTEGER NOT NULL
#        )  
#    """    
#)
#
##commit the transaction 
#conn.commit()
#
##close the connection 
#conn.close()

#cursor.execute("""
#        INSERT INTO AandT (TagNo, LL_Trip, L_Trip, H_Trip, HH_Trip, ALMPR)
#    VALUES
#        ("LDFH6534", 20.1, 5, 5, 20.9, 1),
#        ("UDFH6534", 2, 3, 8, 9, 2)
#""")
#conn.commit()
#conn.close()
#
cursor.execute("""
    SELECT * FROM AlarmData
""")

#fetch the results
results = cursor.fetchall()

#print the results
for row in results:
    print(row)

conn.close()