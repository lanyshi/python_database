import mysql.connector
from mysql.connector import errorcode

# Connect to server
def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        database="my_db",
        user="username",
        password="password")
    # Get a cursor
    cur = cnx.cursor()
    return cnx, cur

# Create table 'pet'
def create_table():
    cnx, cur = connect()

    table_name = "pet"
    table_description = (
    "CREATE TABLE pet ("
    "  name varchar(20),"
    "  owner varchar(20),"
    "  species varchar(20),"
    "  sex char(1)"
    ")")

    try:
        print("Creating table {}: ".format(table_name), end='')
        cur.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    # Close cursor
    cur.close()
    # Close connection
    cnx.close()

# Insert a new row to 'pet'
def insert(name, owner, species, sex):
    cnx, cur = connect()

    try:
        add_pet = ("INSERT INTO pet "
                   "(name, owner, species, sex) "
                   "VALUES (%s, %s, %s, %s)")
        data_pet = (name, owner, species, sex)

        # Insert new pet
        cur.execute(add_pet, data_pet)
        # Make sure data is committed to the database
        cnx.commit()

        cur.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)

# Select the first row in 'pet'
def select_one():
    cnx, cur = connect()

    try:
        # Execute a query
        cur.execute("SELECT * FROM pet")

        # Fetch one result
        row = cur.fetchone()
        print("{} {} {} {}".format(row[0], row[1], row[2], row[3]))
        cur.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)

# Select all rows in 'pet'
def select_all():
    cnx, cur = connect()

    try:
        # Execute a query
        cur.execute("SELECT * FROM pet")

        # Fetch one result
        for (name, owner, species, sex) in cur:
            print("{} {} {} {}".format(name, owner, species, sex))
        cur.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)

# Main
create_table()
insert('coco', 'amanda', 'cat', 'F')
select_one()
insert('kiki', 'jack', 'parrot', 'F')
select_all()
