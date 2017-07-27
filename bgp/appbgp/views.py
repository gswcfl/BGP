# Create your views here.
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
import MySQLdb

def index(request):
	ip_info = []
	address_info = []
	system_info = []
	result_info = []
	time_info = []
	db = MySQLdb.connect('10.52.249.100','bgp_user','111111','reuslt_info')
	cursor = db.cursor()
	sql = "select * from bgp_info;"
	number = cursor.execute(sql)
	n = cursor.fetchall()
	db.commit()
	for i in n:
		ip_info.append(i[0])
		address_info.append(i[1])
		system_info.append(i[2])
		result_info.append(i[3])
		time_info.append(i[4])
		l3 = zip(ip_info,address_info,system_info,result_info,time_info)
	return render_to_response('index.html',{'l3':l3,'number':number})
	#return render_to_response('index.html',{'ip_info':ip_info,'address_info':address_info,'system_info':system_info,'result_info':result_info,'time_info':time_info})
