#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbConnection as dbcon
import unittest

class TestTableFunctions(unittest.TestCase):

	def setUp(self):
		self.tableOneName = ('TestTableOne')
		self.tableOneColumns = dict(ColumnOne='TEXT',ColumnTwo='INTEGER')
		self.tableTwoName = ('TestTableTwo')
		self.tableTwoColumns = ['ColumnOne', 'ColumnTwo']

	def test_connection(self):
		print ('Testing connection')
		self.db = dbcon.Database('test_tables')
		self.assertTrue(self.db.database, 'Test')
		
	def test_create_table_dict(self):
		print ('Testing creating a table using a dictionary')
		self.test_connection()
		self.db.createTable(self.tableOneName, self.tableOneColumns, [])
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertTrue(dbcon.Database.tableExists(self.cur, self.tableOneName))

	def test_create_table_list(self):
		print ('Testing creating a table using a list')
		self.test_connection()
		self.db.createTable(self.tableTwoName, self.tableTwoColumns, [])
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertTrue(dbcon.Database.tableExists(self.cur, self.tableTwoName))

	def test_table_dict(self):
		print ('Testing dictionary table')
		self.test_connection()
		self.db.selectFrom(self.tableOneName)
		self.assertTrue(True)

	def test_table_list(self):
		print ('Testing list table')
		self.test_connection()
		self.db.selectFrom(self.tableTwoName)
		self.assertTrue(True)

	def test_table_unique_columns(self):
		print ('Testing unique columns')
		self.test_connection()

	def test_table_alter(self):
		print ('Testing alter table')
		self.test_connection()

	def test_table_column_alter(self):
		print ('Testing alter column')
		self.test_connection()

	def test_table_constraints(self):
		print ('Testing table constraints')
		self.test_connection()
'''
	def tearDown(self):
		print ('Testing dropping tables')
		self.test_connection()
		self.db.dropTable(self.tableOneName)
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertFalse(dbcon.Database.tableExists(self.cur, self.tableOneName))
		
		self.db.dropTable(self.tableTwoName)
		self.assertFalse(dbcon.Database.tableExists(self.cur, self.tableTwoName))
''''''
class TestQueryFunctions(unittest.TestCase):

	def setUp(self):
		self.db = dbcon.Database('test_queries')
		self.tableOneName = 'TestTableOne'
		self.tableOneColumns = dict(ColumnOne='TEXT',ColumnTwo='INTEGER')
		self.db.createTable(self.tableOneName, self.tableOneColumns)

	def test_query_select(self):
		print ('Testing select from menthod')

	def test_query_where(self):
		print ('Testing select from where') 
	def test_table_insert(self):
		print ('Testing insertion')

	def test_table_update(self):
		print ('Testing Update function')
'''
if __name__ == '__main__':
    unittest.main()
