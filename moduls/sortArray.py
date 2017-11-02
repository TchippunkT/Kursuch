#!/usr/bin/python3
#-*- coding: utf-8 -*-

def _changeElements( array, number ):
	for i in array :
		i[number], i[number+1] = i[number+1], i[number]
	return array

def sortArray( array ):
	# print('begin')
	# print('array: ',array[0])
	for x in range( len(array[0]) ):
		for i in range( len(array[0])-1 ):
			if array[0][i] > array[0][i+1] :
				array = _changeElements( array, i )
			# print('step ',i,'array: ', array[0])
	return array
