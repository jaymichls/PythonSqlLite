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
	
	'''
	Attempts to connect to and sql lite database.
	'''			
	def connectToDB(self):
		# Check to see if there is already an existing connection
		
		if self.con:
			if self.debug:print('Connection already exists.')
			return
		
		try:			
			self.con = self.lite.connect(self.database)
			if self.debug:print('Connection established.')
		except self.lite.Error as e:
			if self.debug:print("SQL Error %s:" % e.args[0])

	'''
	closes an open datbase connection.
	'''
	def closeDB(self):
		if self.con:
			self.con.close()
			print('Connection Closed.')
	
	def createSchema(self, schema): 
		#TODO take a list of dictionaries and create each table seperatly. 
		#might have to be a touple of tablename dictionary pairs, or dictionary of dictionaries. 
		# might want to accecpt a better way to store the schema. 
		
		#Two options of creation might be good having 
		'''
		column, type
		column1, type 
		'''
		#for table in schema:
		#	createTable(table,)
		return
	
	'''
	Creates a table with the provided table name and columns
	that can either be a dictionary or list. unique columns can 
	also be passed and if a duplicate is inserted it updates the 
	origional
	'''
	def createTable(self, tableName, listOfColsAndTypes, uniqueColumns=[]):
		# TODO: Create a table given the table SELECT "test" FROM tvShowame and the columns and column types.
		# maybe pass colname type as a string need to be separated by ','
		if self.con:
			with self.con:
				cur = self.con.cursor()	
				if not self.tableExists(cur, tableName):
					print('Creating Table:',tableName)
					query = "CREATE TABLE IF NOT EXISTS %s("%(tableName)

					# append the columns from a dictionary with their types.	
					if type(listOfColsAndTypes) == dict:
						for column, dataType in listOfColsAndTypes.items():
							# append a comma to seperat values
							if not query.endswith('('): query += ','	
							query += "%s %s"%(column, dataType)
						
					# append the columns from a list with no specific type associated. 
					elif type(listOfColsAndTypes) == list:
						for column in listOfColsAndTypes:
							if not query.endswith('('): query += ','
							query += "%s"%(column)
					
					# handle primary keys in sql lite with unique columns. 
					# if row on insertion exists it gets updated not duplicated. 
					if uniqueColumns:
						query += ", UNIQUE ("
						for column in uniqueColumns:
							# append a comma to seperat values
							if not query.endswith('('): query += ','
							query += "%s"%(column)
						query += ") ON CONFLICT REPLACE"
						
					query += ")"
					
					if self.debug:print(query)
						
					cur.execute(query)
		else:
			noConnection()
			
	'''
	drops the table name passed.
	'''
	def dropTable(self, tableName):
		if self.con:
			with self.con:
				cur = self.con.cursor()
				if self.tableExists(cur, tableName):
					cur.execute("DROP TABLE %s"%(tableName))
					if self.debug:print("Table %s was dropped."%(tableName))

	'''
	simple selet from table name no clauses handled. 

	'''
	def selectFrom(self, tableName): 
		#TODO look into row factory and text factory 
		# might want to check in addition to the table existing that it's only one word to prevent sqli
		if self.con:
			with self.con:
				cur = self.con.cursor()
				if self.tableExists(cur, tableName):
					for row in cur.execute("SELECT * FROM %s"%(tableName)):
						if self.debug:print(row)
						#TODO nothing is done with the results from the query. 

	'''
	using a dictionary of values insert into the tablename provided.  
	no error checking has been preformed at the moment on dictionary.
	if column names don't exist sql throws an exception.
	'''
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
					
					if self.debug:print(query)
					
					cur.execute(query)
					self.con.commit()
	
	def executeQuery(self, query):
		if self.con:
			with self.con:
				cur = self.con.cursor()
				for row in cur.execute(query):
					print (row)
					for column in row:
						print (type(column))

	@staticmethod
	def getCursor(db):
		if db.con:
			with db.con:
				return db.con.cursor()

	def noConnection(self):
		#Something should happen if there is no connection. 
		if self.debug:print('There is no connection, attempting to connect.')
		connectToDB(self)
	
	@staticmethod
	def tableExists(cur, tableName):
		try:			
			cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='%s'"%(tableName))
			if cur.fetchone()[0] == 1: 
				return True
		except Exception as e:                        
			print("An Sql error occured: ",e.args[0])
		return False
			
