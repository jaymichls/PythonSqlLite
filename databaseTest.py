#!/usr/bin/python
# -*- coding: utf-8 -*-

#Database Test

import dbConnection as dbcon

testDB = dbcon.Database ('testDB')

testTable = dict(ShowName='TEXT',Rating='INTEGER') 

testValues = dict(ShowName='Big Bang Theory', Rating='9.4')

print testValues
table = 'tvShow'

# Drop table for testing 
#testDB.dropTable(table)

#testDB.createTable(table,testTable) 

testDB.insertInto(table, testValues)

#testDB.selectFrom(table)

testDB.closeDB()


# SELECT * FROM tvShow
# SELECT 1 FROM sqlite_master WHERE type='table' AND name='tvShow'
## CREATE TABLE tvShow (test)


