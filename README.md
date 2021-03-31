# Handling MySQL and MongoDB databases with Python
Basic data handling with Python, MySQL and MongoDB

Python verion: 3.9.1

Find data handling with Java [here](https://github.com/lanyshi/java_database).

## MySQL
Packages needed: [mysql-connector-python 8.0.18](https://pypi.org/project/mysql-connector-python/8.0.18/)

First install mysql connector using ```pip install mysql-connector-python==8.0.18``` since 8.0 is the only version that's compatible with Python 3.9.

Put ```import mysql.connector``` in the python script.

The program is able to create a table ```pet```.

Field | Type | Null | Key | Default | Extra
------|------|------|-----|---------|------
name | varchar(20) | YES  |     | NULL    |
owner   | varchar(20) | YES  |     | NULL    |
species | varchar(20) | YES  |     | NULL    |
sex     | char(1)     | YES  |     | NULL    |

A message will appear if ```pet``` already exists.

Then the program is able to:
* Select the first row from the table
* Select all rows from the table
* Insert new rows into the table

## MongoDB
Packages needed: [pymongo 3.11.3](https://pypi.org/project/pymongo/)

First ```import pymongo```, then the program is able to
* Connect to database
* Connect to collection
* Find the first document in the collection
* Find all documents in the collection
* Find specific documents in the collection based on certain values
* Delete documents based on certain values
* Delete all documents
* Drop the collection
