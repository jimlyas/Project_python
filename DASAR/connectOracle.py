import cx_Oracle

con = cx_Oracle.connect('hr','password','localhost:1521/XE')
cur = con.cursor()
cur.execute('select * from countries')

for row in cur:
    print(row[0],'\t',row[1])

cur.close()
con.close()