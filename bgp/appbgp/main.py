#!/usr/bin/env python
#-*- coding:utf-8 -*-
import MySQLdb
import os
import commands
import pexpect
import telnetlib
import time
import threading
import sys
sys.path.append(os.path.dirname(os.path.abspath('__file__')))
from huawei_h3c_ssh import huawei_h3c_ssh
from huawei_h3c_telnet import huawei_h3c_telnet
from FiberHome import FiberHome_telnet

#######################################################################################################################
def ping_test(ip_info):
	"""
	ping check function.
	"""
	command = 'ping ' + ip_info + ' -c 2 -i 0.2 -w 0.2'
	(status,output) = commands.getstatusoutput(command)
	if status == 0:
		return "True"
	else:
		return "False"

#######################################################################################################################

if __name__ == "__main__":
	#	"10.192.7.130":["北京电信大郊亭163","扩展二套系统"],
	#	"10.192.23.2":[""],
	#	"10.192.23.130":[""],
	#	"10.192.35.90":["北京铁通西客站","扩展一套系统"],
	#	"10.192.128.20":[""],
	#	"10.192.128.23":[""],
	#	"10.192.131.26":[""],
	#	"10.192.133.30":[""],
	#	"10.192.217.2":[""],
	#	"10.192.217.130":["",],
	#	"10.192.213.2":["广州南方基地302","扩展一套系统"],
	#	"10.192.213.130":["广州南方基地302","扩展二套系统"],
	#	"10.192.215.2":["广州南方基地304","扩展一套系统"],
	#	"10.192.215.130":["广州南方基地304","扩展二套系统"],
	#	"10.192.96.20":[""],
	#	"10.192.96.23":[""],
	#	"10.192.149.2":["上海移动武胜","扩展一套系统"],
	#	"10.192.149.130":["上海移动武胜","扩展二套系统"],
	#	"10.192.145.2":["上海联通金桥三期","扩展一套系统"],
	#	"10.192.145.130":["上海联通金桥三期","扩展二套系统"],
	#"10.192.217.2":["广州联通东莞","扩展一套系统","TELNET","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
	#"10.192.217.130":["广州联通东莞","扩展二套系统","TELNET","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#
#	password_info = {
#		"10.192.15.130":["北京移动大白楼","扩展二套系统","TELNET","FiberHome","hsoft123","Banner@2015","null","show ip bgp summary"],
#		"10.192.15.2":["北京移动大白楼","扩展一套系统","TELNET","FiberHome","hsoft123","Banner@2015","null","show ip bgp summary"],
#		"10.192.21.130":["北京移动三台IP专网","扩展二套系统","TELNET","HUAWEI","hsoft","hsoft","null","display bgp peer"],
#		"10.192.21.2":["北京移动三台IP专网","扩展一套系统","TELNET","HUAWEI","hsoft","hsoft","null","display bgp peer"],
#		"10.192.35.50":["北京联通电报CNC","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.37.54":["北京联通电报CNC","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.17.2":["北京联通东古城","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.17.130":["北京联通东古城","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.11.2":["北京联通沙河","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.11.130":["北京联通沙河","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.35.18":["北京电信西单CN2","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.37.22":["北京电信西单CN2","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.7.2":["北京电信大郊亭163","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.37.94":["北京铁通西客站","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.29.2":["北京科技软件园","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.29.130":["北京科技软件园","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.27.2":["北京教育清华","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.27.130":["北京教育清华","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.34":["广州联通科学城169","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.38":["广州联通科技城169","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.50":["广州联通科学城CNC","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.54":["广州联通科学城CNC","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.2":["广州电信天河163","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.6":["广州电信天河163","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.10":["广州电信同和163","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.14":["广州电信同和163","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.18":["广州电信同和CN2","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.22":["广州电信同和CN2","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.66":["广州移动清河东","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.70":["广州移动清河东","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.131.90":["广州铁通东山","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.133.94":["广州铁通东山","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.26":["上海联通通联169","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.30":["上海联通通联169","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.50":["上海联通通联CNC","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.54":["上海联通通联CNC","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.34":["--上海联通金桥","扩展一套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.38":["--上海联通金桥","扩展二套系统","SSH","H3C","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.2":["上海电信武胜163","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.6":["上海电信武胜163","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.10":["上海电信信息园163","扩展一套系统","TELNET","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.14":["上海电信信息园163","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.99.18":["上海电信民生CN2","扩展一套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g1","display bgp peer"],
#		"10.192.101.22":["上海电信民生CN2","扩展二套系统","SSH","HUAWEI","adminjt","j0t0x5t","2k0s1k3g2","display bgp peer"],
#		"10.192.147.2":["上海移动迎春路","扩展一套系统","TELNET","FiberHome","adminjt","j0t0x5t","nll","show ip bgp summary"],
#		"10.192.147.130":["上海移动迎春路","扩展二套系统","TELNET","FiberHome","adminjt","j0t0x5t","nll","show ip bgp summary"]
#	}

	ip_info = ""
	address_info = ""
	system_info = ""
	login_info = ""
	changjia_info = ""
	username_info = ""
	password1_info = ""
	password2_info = ""
	command_info = ""
	result = []
	db = MySQLdb.connect('10.52.249.100','admin_user','111111','password_info')
	cursor = db.cursor()
	sql = "select * from password;"
	cursor.execute(sql)
	n = cursor.fetchall()
	db.commit()
	for i in n:
		ip_info = i[0]
		address_info = i[1]
		system_info = i[2]
		login_info = i[3]
		changjia_info = i[4]
		username_info = i[5]
		password1_info = i[6]
		password2_info = i[7]
		#command_info = password_info[i][7]
		#print ip_info+"\t"+address_info +"\t"+system_info+"\t"+ login_info+"\t"+ changjia_info+"\t"+ username_info+"\t"+ password1_info+"\t"+ password2_info+"\t"+ command_info
		if ping_test(ip_info):
			#print ip_info +"\t"+ "True"
			if changjia_info == "HUAWEI" and login_info == "SSH":
				t = threading.Thread(target=huawei_h3c_ssh,args=(ip_info,address_info,system_info,username_info,password1_info,password2_info,"display bgp peer"))
				result.append(t)
			elif changjia_info == "HUAWEI" and login_info == "TELNET":
				t = threading.Thread(target=huawei_h3c_telnet,args=(ip_info,address_info,system_info,username_info,password1_info,password2_info,"display bgp peer"))
				result.append(t)
			elif changjia_info == "H3C" and login_info == "SSH":
				t = threading.Thread(target=huawei_h3c_ssh,args=(ip_info,address_info,system_info,username_info,password1_info,password2_info,"display bgp peer"))
				result.append(t)
			elif changjia_info == "H3C" and login_info == "TELNET":
				t = threading.Thread(target=huawei_h3c_telnet,args=(ip_info,address_info,system_info,username_info,password1_info,password2_info,"display bgp peer"))
				result.append(t)
			elif changjia_info == "FiberHome" and login_info == "TELNET":
				t = threading.Thread(target=FiberHome_telnet,args=(ip_info,address_info,system_info,username_info,password1_info,password2_info,"show ip bgp summary"))
				result.append(t)
		else:
			db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
			cursor = db.cursor()
			sql = ('update bgp_info set result="ping timeout...",time_info="%s" where ip_info="%s";' %(time.strftime("%Y-%m-%d %H:%M:%S"),ip_info))
			cursor.execute(sql)
			db.commit()
			db.close()
			#f = file("result.txt","a+")
			#f.write(str(ip_info)+"#"+str(address_info)+"#"+str(system_info)+"#"+"ping timeout"+"#"+str(time.strftime("%Y-%m-%d %H:%M:%S"))+"\n")
			#print ip_info +"\t"+ "ping timeout" + address_info + system_info
			#f.flush()
			#f.close()
	for i in range(len(result)):
		result[i].start()
	for i in range(len(result)):
		result[i].join()
