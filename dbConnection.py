#!/usr/bin/python
# -*- coding: utf-8 -*-


class Database:
	import sqlite3 as lite
	con = None 
	#TODO 
	
	def __init__(self, database):
		self.database = database
		connectToDB(self, self.database)
		
	def connectToDB(self, database):
		# Check to see if there is already an existing connection
		if self.con:
			return
		
		try:
			self.con = lite.connect(database)
		except lite.Error, e:
			print "SQL Error %s:" % e.args[0]
			
	def closeDB(self):
		if self.con:
			con.close()
	
	def createSchema(self, schema): 
	#TODO figure out how to store the schema
		return
	
	def createTable(self, tableName, listOfColsAndTypes, colsAndTypes):
		# TODO: Create a table given the table name and the columns and column types.
		# maybe pass colname type as a string need to be separated by ','
		if self.con:
			with self.con:
				cur = self.con.cursor()
				cur.execute("CREATE TABLE %s(%s)"%s(tableName, colsAndTypes))
