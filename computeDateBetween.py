#! /usr/bin/python
 #-*- coding: utf-8 -*
 #"encoding":"cp936"

def dateAbs(a,b):

	"the date between different y,m,d but with same y and m"
	if a >= b:
		return (a-b)-1

	else :
		return (b-a)-1

def isLeap(year):
	"if it is leap year?"
	if (year%4==0 ) and (year%100!=0 or year%400 ==0) :
		return 1
	else:
		return 0

def Days(y,m,d):
	"the count of date(y m d) from Janurary 1st"
	days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
	sum = 0
	if isLeap(y):
		days[2] = 29
	for i in days[0:m]:
		sum = sum + i
	'''sum = sum + d - 1'''
	sum = sum + d
	'''print sum'''

	return sum

def diffDays(y1,m1,d1,y2,m2,d2):
	"the count of days between y1m1d1 and y2m2d2"
	
	sum = 0
	if y1 == y2 :
		
		"the date between different y,m,d only with same y "
		s1 = Days(y1,m1,d1)
		s2 = Days(y2,m2,d2)
		sum = dateAbs(s1,s2)
		print "the count between %d/%d/%d and %d/%d/%d is %d days" %(y1,m1,d1,y2,m2,d2,sum)
		return sum


	elif y1 < y2 :
			count = y2 - y1
			
			"计算y1到年末的时间p1+计算y1年末到y2年初的时间p1+计算y2年到ymd的日子p3"
			t1 = Days(y1,m1,d1)
			t2 = Days(y2,m2,d2)

			p1=Days(y1,12,31)-t1
			"p1 counts the days from y1m1d1 to end of y1"
			'''print Days(y1,12,31)-t1'''
			'''print d'''
			sum = 0
			for i in range(count-1):
				sum=sum+Days(y1+i,12,31)
				'''print sum'''
			p2=sum
			"p2 counts the days of bewteen years "
			'''print p2'''
			p3=t2-1
			"p3 counts the days before y2m2d2 "
			sum = p1 + p2 + p3

			print "the count between %d/%d/%d and %d/%d/%d is %d days" %(y1,m1,d1,y2,m2,d2,sum)

			return sum
	else:
		y1,m1,d1 = y2,m2,d2
		diffDays(y1,m1,d1,y2,m2,d2)

	'''print sum'''


print "this is a demo of func 'diffDays(y1,m1,d1,y2,m2,d2)':"
diffDays(2018,1,1,2018,1,3)




