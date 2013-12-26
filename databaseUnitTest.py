#!/usr/bin/python
# -*- coding: utf-8 -*-

import dbConnection as dbcon
import unittest

class TestTableFunctions(unittest.TestCase):

	def setUp(self):
		self.db = dbcon.Database('Test')
		self.tableOne = dict(ColumnOne='TEXT',ColumnTwo='INTEGER')
		self.tableName = 'TestTable'

	def test_create(self):
		self.db.createTable(self.tableName, self.tableOne, [])
		self.cur = dbcon.Database.getCursor(self.db)
		self.assertTrue(dbcon.Database.tableExists(self.cur, self.tableName))

if __name__ == '__main__':
    unittest.main()