#! /usr/bin/python
 #-*- coding: utf-8 -*
 #"encoding":"cp936"

def dateAbs(a,b):

	"日期之差"
	if a >= b:
		print " countnum is: %d " %(a-b)
		return (a-b)

	else :
		print "countnum is :%d " %(b-a)
		return (b-a)

def isLeap(year):
	"判断是否是闰年"
	if (year%4==0 ) and (year%100!=0 or year%400 ==0) :
		return 1
	else:
		return 0

def Days(y,m,d):
	"判断某个日期从年初（y年1月1日）到该天（y年m月d天）的天数"
	days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	sum = 0
	if isLeap(y):
		days[2] = 29
	for i in days[0:m]:
		sum = sum + i
	sum = sum + d - 1
	print sum

	return sum

def diffDays(y1,m1,d1,y2,m2,d2):
	"判断两个日期之间的天数"
	
	sum = 0
	if y1 == y2 :
		
		"同年不同月不同日"
		s1 = Days(y1,m1,d1)
		s2 = Days(y2,m2,d2)
		sum = dateAbs(s1,s2)
		return sum


	elif y1 < y2 :
			count = y2 - y1
			
			"计算y1到年末的时间p1+计算y1年末到y2年初的时间p1+计算y2年到ymd的日子p3"
			t1 = Days(y1,m1,d1)
			t2 = Days(y2,m2,d2)

			p1=Days(y1,12,31)-t1+1
			'''print Days(y1,12,31)-t1'''
			'''print d'''
			sum = 0
			for i in range(count-1):
				sum=sum+Days(y1+i,12,31)+1
				'''print sum'''
			p2=sum
			'''print p2'''
			p3=t2
			sum = p1 + p2 + p3

			print sum

			return sum
	else:
		y1,m1,d1 = y2,m2,d2
		diffDays(y1,m1,d1,y2,m2,d2)

	'''print sum'''

'''
print "Please input the dates you want to input:"

y1= raw_input("year1:")
print "that's ok "
m1= raw_input("month1:")
d1= raw_input("day1:")
y2= raw_input("year2:")
m2= raw_input("month2:")
d2= raw_input("day2:")
'''

diffDays(2018,1,1,2018,1,3)



