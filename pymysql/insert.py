import pymysql

s1 = 'Jack'
a1 = 12

conn=pymysql.connect(host='127.0.0.1', user='u', passwd='p', db='d', port=3306)
cur=conn.cursor()

sql_insert ="""
            INSERT INTO table_name (student,age)
            VALUES ('%s', '%s')
        """ % (s1,a1)

cur.execute( sql_insert )  
conn.commit()

cur.close()
conn.close()