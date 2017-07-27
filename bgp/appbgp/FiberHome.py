#/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
import commands
import pexpect
import time
import telnetlib
import re

def FiberHome_telnet(ip_info,address_info,system_info,username_info,password1_info,password2_info,command_info):
	try:
		tn = telnetlib.Telnet(ip_info)
		time.sleep(1)
		tn.read_until("Username:")
		tn.write(username_info + "\r\n")
		tn.read_until("Password:")
		tn.write(password1_info + "\r\n")
		if password2_info != "null":
			tn.write("enable\r\n")
			tn.write(password2_info + "\r\n")
		else:
			tn.write("enable\r\n")
		time.sleep(1)
		r1 = tn.read_very_eager()
		time.sleep(1)
		tn.write(command_info + "\r\n")
		time.sleep(2)
		r2 = tn.read_very_eager()
		#print ip_info+" :",address_info,system_info
		#print r2
		#print "\n"
		tn.close()
		r3 = r2.split("\n")
		bgp_result = []
		for i in r3:
			info = i.split()
			#p = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9][01]?[0-9][0-9]?)$")
			p = re.compile("((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))")
			if info != []:
				if p.match(info[0]):
					bgp_result.append(i)
		#print "\n"
		#print ip_info+"#"+address_info+"#"+system_info+"#"+str(bgp_result)+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))
		#f = file("result.txt","a+")
		db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
		cursor = db.cursor()
		sql = ('update bgp_info set result="%s",time_info="%s" where ip_info="%s";' %(bgp_result,time.strftime("%Y-%m-%d %H:%M:%S"),ip_info))
		cursor.execute(sql)
		db.commit()
		db.close()
		#print sql
		#f.write(str(ip_info)+"#"+str(address_info)+"#"+str(system_info)+"#"+str(bgp_result)+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"\n")
		#f.flush()
		#f.close()
	except Exception as e:
		alert = "Error : login failed"
		db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
		cursor = db.cursor()
		sql = ('update bgp_info set result="%s",time_info="%s" where ip_info="%s";' %(alert,time.strftime("%Y-%m-%d %H:%M:%S"),ip_info))
		cursor.execute(sql)
		#print sql
		db.commit()
		db.close()
		#bgp_result = []
		#bgp_result.append(alert)
		#f = file("result.txt","a+")
		#f.write(str(ip_info)+"#"+str(address_info)+"#"+str(system_info)+"#"+str(bgp_result)+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"\n")
		#f.flush()
		#f.close()
		#print bgp_result
		#print ip_info+" :",alert
		#print alert
if __name__ == "__main__":
	ip_info = "10.192.15.2"
	address_info = ""
	system_info = ""
	username_info = "hsoft123"
	password1_info = "Banner@2015"
	password2_info = "null"
	command_info = "show ip bgp summary"
	FiberHome_telnet(ip_info,address_info,system_info,username_info,password1_info,password2_info,command_info)
