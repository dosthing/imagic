#! /usr/bin/env python

from distutils.log import warn as printf
from json import dumps
from pprint import pprint

BOOKs = {
	'2019010101':{
		'tilte':'Core Python Programming',
		'edition':2,
		'year':2019,
	},
	'2019010102':{
	'title':'Python web Development with Django',
	'authors':['Jeff Forcier','Pual Bissex','Wesley Chun'],
	'year':2019,
	},
	'2019010103':{
	'title':'Python Fundamenttals',
	'year':2019,
	},
}
printf(' RAW DICT')
printf('BOOKs')

printf('\n PRETTY_PRINTEDDICT')
pprint(BOOKs)

printf('\n RAW JSON')
printf(dumps(BOOKs))

printf('\n PRETTY_PRINTEDJSON')
printf(dumps(BOOKs,indent=4))