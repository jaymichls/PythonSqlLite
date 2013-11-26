#!/usr/bin/python
# -*- coding: utf-8 -*-

class Database:
	import sqlite3 as lite
	
	#TODO 
	
	def __init__(self, database):
		self.database = database
		self.con = None
		self.connectToDB()
		
	def connectToDB(self):
		# Check to see if there is already an existing connection
		
		if self.con:
			print 'Connection already exists'
			return
		
		try:
			self.con = self.lite.connect(self.database)
			print 'Connection established'
		except self.lite.Error, e:
			print "SQL Error %s:" % e.args[0]
			
	def closeDB(self):
		if self.con:
			self.con.close()
			print 'Connection Closed'
	
	def createSchema(self, schema): 
	#TODO figure out how to store the schema
		return
	
	def createTable(self, tableName, listOfColsAndTypes):
		# TODO: Create a table given the table name and the columns and column types.
		# maybe pass colname type as a string need to be separated by ','
		if self.con:
			with self.con:
				cur = self.con.cursor()
				print listOfColsAndTypes				
				cur.execute("CREATE TABLE %s(test text)"%(tableName))
	
	def dropTable(self, tableName):
		if self.con:
			with self.con:
				cur = self.con.cursor()
				cur.execute("DROP TABLE %s"%(tableName))

	def selectFrom(self, tableName): 
		#TODO look into row factory and text factory 
		if self.con:
			with self.con:
				cur = self.con.cursor()
				for row in cur.execute("SELECT * FROM %s"%(tableName)):
					print row
								
	def insertInto(self, tableName, value):
		if self.con:
			with self.con:
				cur = self.con.cursor()
				print value
				cur.execute("INSERT INTO %s VALUES('sweet')"%(tableName))
				self.con.commit()
