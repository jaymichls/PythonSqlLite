#!/usr/bin/python
# -*- coding: utf-8 -*-

#Database Test

import dbConnection as dbcon


testDB = dbcon.Database ('testDB')

testTable = dict(ShowName='TEXT',Rating='TEXT') 
table = 'tvShow'

# Drop table for testing 
testDB.dropTable(table)


print testDB.con
testDB.createTable(table,testTable) 

print 'insert'
testDB.insertInto(table, 'sweet')

print 'select'
testDB.selectFrom(table)

testDB.closeDB()

