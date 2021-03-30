# Handling MySQL and MongoDB databases with Python
Basic data handling with Python, MySQL and MongoDB

Python verion: 3.9.1

Find data handling with Java [here](https://github.com/lanyshi/java_database).

## MySQL
```import mysql.connector``` by installing connector using ```pip install mysql-connector-python==8.0.18``` since 8.0 is the only version that's compatible with Python 3.9.

First create a table ```pet```.

Field | Type | Null | Key | Default | Extra
------|------|------|-----|---------|------
name | varchar(20) | YES  |     | NULL    |
owner   | varchar(20) | YES  |     | NULL    |
species | varchar(20) | YES  |     | NULL    |
sex     | char(1)     | YES  |     | NULL    |

A message will appear if ```pet``` already exists.

Then the program is able to:

* Select the first row from the table.
* Select all rows from the table.
* Insert new rows into the table.
