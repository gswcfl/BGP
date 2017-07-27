#/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import commands
import pexpect
import time
import telnetlib
import re

def huawei_h3c_ssh(ip_info,address_info,system_info,username_info,password1_info,password2_info,command_info):
	try:
		ssh = pexpect.spawn('ssh %s@%s' %(username_info,ip_info))
		i = ssh.expect(['password:','Are you sure you want to continue connecting (yes/no)?'],timeout=5)
		time.sleep(1)
		if i == 0:
			ssh.sendline(password1_info)
		elif i == 1:
			ssh.sendline('yes')
			ssh.expect('password:')
			ssh.sendline(password1_info)
		time.sleep(1)
		if password2_info != "null":
			ssh.sendline('super')
			ssh.sendline(password2_info)
		time.sleep(1)
		ssh.expect('>')
		r1 = ssh.before
		ssh.sendline(command_info)
		ssh.expect(command_info)
		ssh.expect('>')
		r2 = ssh.before
		#print ip_info + ":",address_info,system_info
		#print r2
		#print "\n"
		r3 = r2.split("\n")
		bgp_result = []
		for i in r3:
			info = i.split()
			#p = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9][01]?[0-9][0-9]?)$")
			p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
			if info != []:
				if p.match(info[0]):
					bgp_result.append(i)
		db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
		cursor = db.cursor()
		sql = ('update bgp_info set result="%s",time_info="%s" where ip_info="%s";' %(bgp_result,time.strftime("%Y-%m-%d %H:%M:%S"),ip_info))
		cursor.execute(sql)
		#print sql
		db.commit()
		db.close()
		#print "\n"
		#f = file("result.txt","a+")
		#f.write(str(ip_info)+"#"+str(address_info)+"#"+str(system_info)+"#"+str(bgp_result)+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"\n")
		#f.flush()
		#f.close()
	except Exception as e:
		alert = "Error : login failed"
		db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
		cursor = db.cursor()
		sql = ('update bgp_info set result="%s",time_info="%s" where ip_info="%s";' %(alert,time.strftime("%Y-%m-%d %H:%M:%S"),ip_info))
		cursor.execute(sql)
		db.commit()
		db.close()
		#bgp_result = []
		#bgp_result.append(alert)
		#f = file("result.txt","a+")
		#f.write(str(ip_info)+"#"+str(address_info)+"#"+str(system_info)+"#"+str(bgp_result)+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"\n")
		#f.flush()
		#f.close()
		#print ip_info+" : ",alert
		#print alert
if __name__ == "__main__":
	ip_info = "10.192.11.2"
	address_info = ""
	system_info = ""
	username_info = "adminjt"
	password1_info = "j0t0x5t"
	password2_info = "2k0s1k3g1"
	command_info = "display bgp peer"
	huawei_h3c_ssh(ip_info,address_info,system_info,username_info,password1_info,password2_info,command_info)
