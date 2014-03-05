#rot13 escaper

#from string import maketrans
import string

def rot(s):
	table = string.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
					  		 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
	table = table.decode("latin-1")
	return s.translate(table)

#print rot(u'kaffe')