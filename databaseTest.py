#!/usr/bin/python
# -*- coding: utf-8 -*-

#Database Test

import dbConnection as dbcon

testDB = dbcon.Database ('testDB')

testTable = dict(ShowName='TEXT',Rating='TEXT') 
table = 'tvShow'

# Drop table for testing 
testDB.dropTable(table)



testDB.createTable(table,testTable) 

testDB.insertInto(table, 'test')

#testDB.selectFrom(table)

testDB.closeDB()


# SELECT 1 FROM tvShow
# SELECT 1 FROM sqlite_master WHERE type='table' AND name='tvShow'