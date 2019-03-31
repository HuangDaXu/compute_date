#! /usr/bin/python
 #-*- coding: utf-8 -*
 #"encoding":"cp936"

def dateAbs(a,b):

	"日期之差"
	if a >= b:
		print "同年不同月不同日结果为：%d 天" %(a-b)
		return (a-b)

	else :
		print "同年不同月不同日结果为：%d 天" %(b-a)
		return (b-a)

def isLeap(year):
	"判断是否是闰年"
	if (year%4==0 ) and (year%100!=0 or year%400 ==0) :
		return 1
	else:
		return 0

'''def yearAlldays():
	if isLeap():
		p=366
	else:
		p=365
	return p
'''

def Days(y,m,d):
	"判断某个日期从年初（y年1月1日）到该天（y年m月d天）的天数"
	days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	sum = 0
	if isLeap(y):
		days[2] = 29
	for i in days[0:m]:
		sum = sum + i
	sum = sum + d - 1
	return sum
'''def day2end(y,m,d):
	"片段某个日期从该天（y天m月d天）到年末（y年12月31日）的天数"
	days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	sum = 0
	if isLeap(y):
		days[2] = 29
	for i in days:
		sum = d + i
'''
def diffDays(y1,m1,d1,y2,m2,d2):
	"判断两个日期之间的天数"
	
	sum = 0
	if y1 == y2 :
		
		"同年不同月不同日"
		s1 = Days(y1,m1,d1)
		s2 = Days(y2,m2,d2)
		sum = dateAbs(s1,s2)
		return sum


	elif y1 > y2 :
			count = y1 - y2
			'''allDays=count*yearAlldays()'''

			'''if count ==1:
			t1 = Days(y1,m1,d1)
			t2 = Days(y2,m2,d2)
			sum=t1-t2+begin2day(y1,12,31)+1
		    print "同年不同月不同日结果为：%d 天" %(a-b)
			return  sum
			'''
		
			"计算y1到年末的时间p1+计算y1年末到y2年初的时间p1+计算y2年初到ymd的日子p3"
			t1 = Days(y1,m1,d1)
			t2 = Days(y2,m2,d2)
			p1=yearAlldays()-t1-1
			p2=count -1
			p3=t2
			sum = p1 + p2 + p3

			return sum
	else:
		y1,m1,d1 = y2,m2,d2
		diffDays(y1,m1,d1,y2,m2,d2)

	print sum



diffDays(2017,1,2,2017,1,3)



