#!/usr/bin/env python
# -*- conding:utf-8 -*-
import MySQLdb
db = MySQLdb.connect('10.52.249.100','admin_user','111111','password_info')
cursor = db.cursor()
sql = "select * from password;"
n=cursor.execute(sql)
db.commit()
print n
