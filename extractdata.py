import sqlite3
import json

db_filename = '/home/student/momohame/dmaproj/cmaartworks.db'
db = sqlite3.connect(db_filename)
cur = db.cursor()

result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
table_names = sorted(list(zip(*result))[0])

rows=[]

for table in table_names:
    if table == 'artwork':
        cur.execute("SELECT * FROM artwork")
        data=cur.fetchall()
        # Created a data list to append the values
        data_list = []
        result = cur.execute("PRAGMA table_info('artwork')").fetchall()
        column_names = list(zip(*result))[1]
        # Tested for printing column names
        print(column_names)
        for d in data:
            tab = ("id: "+d[0],"accession number: "+d[1],"title: "+d[2],"tombstone: "+d[3])
            #print("id : " +d[0])
            data_list.append(tab)
        output =json.dumps(data_list, indent=2)
        # For your reference in terminal
        print(output)
        # Opening a text document to wirte the output
        with open('/home/student/momohame/dmaproj/artworks.txt', 'w') as f:
         print (output, file = f)
      
# In local the text file is opening. So I have written the code below for local. The output will be in artworks.txt. I will turn in three files.
#if __name__ == "__main__":

#    import sqlite3
#    import json
#    with open('/Users/Gani/Desktop/DB project/Extract table and colums/artworks.txt', 'a') as f:
#       dbname = '/Users/Gani/Desktop/DB project/Extract table and colums/cmaartworks.db'
#       try:
#          print ("INITILIZATION...")
#          con = sqlite3.connect(dbname)
#          cursor = con.cursor()
#          cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#          tables = cursor.fetchall()
#          for tbl in tables:
#             #print ("\n########  "+tbl[0]+"  ########")
#             cursor.execute("SELECT * FROM "+tbl[0]+";")
#             row_headers=[x[0] for x in cursor.description] #this will extract row headers
#             rv = cursor.fetchall()
#             json_data=[]
#             for result in rv:
#                json_data.append(dict(zip(row_headers,result)))
#                #print (json.dumps(json_data), file = f)
#                print (json.dumps(json_data, indent = 2), file = f)
#       except KeyboardInterrupt:
#          print ("\nClean Exit By user")
#       finally:
#          print ("\nEnd.\n")