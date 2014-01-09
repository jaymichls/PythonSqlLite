#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbConnection as dbcon
import unittest

class TestTableFunctions(unittest.TestCase):

	def setUp(self):
		self.tableOneName = 'TestTableOne'
		self.tableOneColumns = dict(ColumnOne='TEXT',ColumnTwo='INTEGER')
		self.tableTwoName = 'TestTableTwo'
		self.tableTwoColumns = ['ColumnOne', 'ColumnTwo']

	def test_connection(self):
		print 'Testing connection'
		self.db = dbcon.Database('Test')
		self.assertTrue(self.db.database, 'Test')
		
	def test_create_table_dict(self):
		print 'Testing creating a table using a dictionary'
		self.test_connection()
		self.db.createTable(self.tableOneName, self.tableOneColumns, [])
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertTrue(dbcon.Database.tableExists(self.cur, self.tableOneName))

	def test_create_table_list(self):
		print 'Testing creating a table using a list'
		self.test_connection()
		self.db.createTable(self.tableTwoName, self.tableTwoColumns, [])
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertTrue(dbcon.Database.tableExists(self.cur, self.tableTwoName))

	def test_table_dict(self):
		print 'Testing dictionary table'
		self.test_connection()
		self.db.selectFrom(self.tableOneName)
		self.assertTrue(True)


	def test_table_list(self):
		print 'Testing list table'
		self.test_connection()
		self.db.selectFrom(self.tableTwoName)
		self.assertTrue(True)


	def tearDown(self):
		print 'Testing dropping tables'
		self.test_connection()
		self.db.dropTable(self.tableOneName)
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertFalse(dbcon.Database.tableExists(self.cur, self.tableOneName))
		
		self.db.dropTable(self.tableTwoName)
		self.assertFalse(dbcon.Database.tableExists(self.cur, self.tableTwoName))

if __name__ == '__main__':
    unittest.main()