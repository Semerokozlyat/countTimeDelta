#!/usr/bin/python

from datetime import datetime
import sys

def getTaskTimeDelta():
	with open('./input_data.txt') as tasksFile:
		for i, line in enumerate(tasksFile):
			rawStartDateTuple = line[1:].split(' ',2)
			dateStart = datetime.strptime(rawStartDateTuple[0] + ' ' + rawStartDateTuple[1] ,"%y-%m-%d %H:%M:%S.%f") if '+++' in rawStartDateTuple[2] else 'None'
			nextLine = tasksFile.next()
			rawEndDateTuple = nextLine[1:].split(' ',2)
			dateEnd = datetime.strptime(rawEndDateTuple[0] + ' ' + rawEndDateTuple[1] ,"%y-%m-%d %H:%M:%S.%f") if '---' in rawEndDateTuple[2] else 'None'
			print("Request  number %s" % str(i+1))
			print(dateStart)
			print(dateEnd)
			print("Time Delta: ")
			print(dateEnd-dateStart)
if __name__ == '__main__':
	getTaskTimeDelta()			
