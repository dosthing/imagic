#! /usr/bin/env python

import csv
from distutils.log import warn as printf
DATA = (
	('id', 'name', 'age','sex','wage'),
	(1, '小李', 24, 'm', '8000'),
	(2, '小王', 25, 'm', '6000'),
	(3, '小杜', 23, 'w', '6000'),
)
printf('*** Write CSV DATA')
f = open('wageinfo.csv','w',newline='')
writer = csv.writer(f)
for record in DATA:
	writer.writerow(record)
	print(record)
f.close()

printf('read csv data')
f = open('wageinfo.csv','r')
reader = csv.reader(f)
for id,name,age,sex,wage in reader:
	printf('id %s: name: %s age: %s sex: %s wage: %s' %(id,name,age,sex,wage))
f.close()