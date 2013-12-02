#!/usr/bin/python
# -*- coding: utf-8 -*-

class Database:
	import sqlite3 as lite
	
	#TODO Maybr should be able to pass a connection object to this class. 
	
	def __init__(self, database):
		if database: self.database = database
		else: return
		self.con = None
		self.debug = 1
		self.connectToDB()
				
	def connectToDB(self):
		# Check to see if there is already an existing connection
		
		if self.con:
			print 'Connection already exists.'
			return
		
		try:			
			self.con = self.lite.connect(self.database)
			print 'Connection established.'
		except self.lite.Error, e:
			if self.debug:print "SQL Error %s:" % e.args[0]
			
	def closeDB(self):
		if self.con:
			self.con.close()
			print 'Connection Closed.'
	
	def createSchema(self, schema): 
	#TODO figure out how to store the schema
		return
	
	def createTable(self, tableName, listOfColsAndTypes):
		# TODO: Create a table given the table SELECT "test" FROM tvShowame and the columns and column types.
		# maybe pass colname type as a string need to be separated by ','
		if self.con:
			with self.con:
				cur = self.con.cursor()	
				if self.tableExists(cur, tableName):
					query = "CREATE TABLE %s("%(tableName)
					for column, dataType in listOfColsAndTypes.items():
						if not query.endswith('('): query += ','	# append a comma to seperat values
						query += "%s %s"%(column, dataType)
					query += ")"
					
					if self.debug:print query 
					
					cur.execute(query)
		else:
			noConnection()
			
	def dropTable(self, tableName):
		if self.con:
			with self.con:
				cur = self.con.cursor()
				if self.tableExists(cur, tableName):
					cur.execute("DROP TABLE %s"%(tableName))
					if self.debug:print "Table %s was dropped."%(tableName)
					
	def selectFrom(self, tableName): 
		#TODO look into row factory and text factory 
		if self.con:
			with self.con:
				cur = self.con.cursor()
				if self.tableExists(cur, tableName):
					for row in cur.execute("SELECT * FROM %s"%(tableName)):
						if self.debug:print row
									
	def insertInto(self, tableName, values):
		# TODO allow insert of one or many columns in any order..
		if self.con:
			with self.con:
				cur = self.con.cursor()
				#cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='%s'"%(tableName))
				#if cur.fetchone() == 1:
				if self.tableExists(cur, tableName):
					query = "INSERT INTO %s ("%(tableName)
					data = ") VALUES ("				
					for column, value in values.items():
						if not query.endswith('('): 
							query += ','	# append a comma to seperat values
							data += ','
							
						query += "%s"%(column)					
						if isinstance(value,str):data += "'%s'"%(value)
						else:data += "%s"%(value)
						
					query += data + ')'
					
					if self.debug:print query
					
					cur.execute(query)
					self.con.commit()
		
	def noConnection(self):
		#Something should happen if there is no connection. 
		if self.debug is 1:print 'There is no connection, attempting to connect.'
		connectToDB(self)
	
	def tableExists(self, cur, tableName):
		try:			
			cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='%s'"%(tableName))
			if cur.fetchone()[0] == 1: 
				return True
		except Exception, e: 
			if self.debug:print "An Sql error occured: ",e.args[0]	
			print "Table:",tableName," doesn't exist"
		return False
			