PythonSqlLite
=============

A wrapper for the python sqlite API.
The idea behind this is to make creating, inserting and querying tables simple using python objects.

this does not currently prevent against sqli although it is an important feature that should be added.

supported:
create table queries with unique columns as primary keys and either a list or dictionary or columns.
drop table.
insert into that takes a dictionary of column value pairs.
static methods:
table exists


