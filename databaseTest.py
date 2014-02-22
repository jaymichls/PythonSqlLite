#!/usr/bin/python
# -*- coding: utf-8 -*-

#Database Test

import dbConnection as dbcon

testDB = dbcon.Database ('testDB')

testTable = dict(ShowName='TEXT',Rating='INTEGER') 

testValues = dict(ShowName='Big Bang Theory', Rating=5)
testValues2 = dict(ShowName='Big Bang Theory', Rating=9.6)

uniqueColumn = ['ShowName']
print (testValues)
table = 'tvShow'

# Drop table for testing 
testDB.dropTable(table)

testDB.createTable(table, testTable, uniqueColumn) 

testDB.insertInto(table, testValues)
testDB.insertInto(table, testValues2)

testDB.selectFrom(table)
testDB.executeQuery('select * from tvShow')
testDB.closeDB()


# SELECT * FROM tvShow
# SELECT 1 FROM sqlite_master WHERE type='table' AND name='tvShow'
## CREATE TABLE tvShow (test)


