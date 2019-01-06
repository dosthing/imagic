#! /usr/bin/env python

from xml.etree.ElementTree import Element,SubElement,tostring
from xml.dom.minidom import parseString

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

books = Element('books')
for isbn,info in BOOKs.items():
	book = SubElement(books,'book')
	info.setdefault('authors','Wesley Chun')
	info.setdefault('edition',1)
	for key,val in info.items():
		SubElement(book,key).text = ', '.join(str(val).split(':'))
		
xml = tostring(books)
print (' RAW XML')
print (xml)

print ('\nPRETTY_PRINTED XML')
dom = parseString(xml)
print (dom.toprettyxml('  '))

print (' FLAT STRUCTURE')
for elmt in books.getiterator():
	print (elmt.tag, '_',elmt.text)
	
print ('\n TITLES ONLY')
for book in books.findall('.//title'):
	print (book.text)