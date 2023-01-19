import sqlite3


def print_full_table_per_row():
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    print("NAME \t\t EMAIL")
    for item in items:
        print(f"{item[0]} {item[1]}:\t {item[2]}")


# Connect to database
# connection = sqlite3.connect(":memory:") # Used to store things in memory without creating a database
connection = sqlite3.connect("customer.db")


# Create a cursor
c = connection.cursor()


# Adding data to the database
# First command
# c.execute("""--sql 
# CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
# );
# """)

# # Second command
# c.execute("""--sql
# INSERT INTO customers
# VALUES ('John', 'Elder', 'john@codemy.com');
# """)

# # Third command
# c.execute("""--sql
# INSERT INTO customers
# VALUES ('Tim', 'Smith', 'tim@codemy.com');
# """)

# # Fourth command
# c.execute("""--sql
# INSERT INTO customers
# VALUES ('Mary', 'Brown', 'mary@codemy.com');
# """)

# # Fifth command
# many_customers = [
#     ("Wes", "Brown", "wes@brown.com"),
#     ("Steph", "Kuewa", "steph@kuewa.com"),
#     ("Dan", "Pas", "dan@pas.com")
# ]

# c.executemany("""--sql
# INSERT INTO customers
# VALUES (?, ?, ?);
# """, many_customers)


# # Datatypes:
# NULL (Kinda like a boolean, if it exists, it's not NULL, if it doesn't exist, it's NULL)
# INTEGER
# REAL (Decimal)
# TEXT
# BLOB (Images, songs, etc. Random shit basically)


# # Uptading records
# c.execute("""--sql
# UPDATE customers
# SET first_name = 'Bobby'
# WHERE last_name = 'Elder';
# """)
# print_full_table_per_row()

# Better update
# c.execute("""--sql
# UPDATE customers
# SET first_name = 'John'
# WHERE rowid = 1;
# """)
# print_full_table_per_row()

# # Bad example
# c.execute("""--sql
# UPDATE customers
# SET first_name = 'Mary'
# WHERE last_name = 'Brown';
# """)
# print_full_table_per_row()

# # Fixing the error
# c.execute("""--sql
# UPDATE customers
# SET first_name = 'Wes'
# WHERE rowid = 4;
# """)
# print_full_table_per_row()


# Deleting data
# c.execute("DELETE FROM customers ") # Deletes EVERYTHING
# c.execute("DELETE FROM customers WHERE rowid = 6")
# print_full_table_per_row()


# # Querying the database
# c.execute("""--sql SELECT rowid, * FROM customers;""")
# # print(c.fetchone())
# # print(c.fetchmany(2))
# items = c.fetchall()
# # print(items)
# print("NAME \t\t EMAIL")
# for item in items:
#     print(f"{item[0]} {item[1]}:\t {item[2]}")

# c.execute("""--sql SELECT * FROM customers WHERE last_name = 'Smith';""")
# items = c.fetchall()
# print("NAME \t\t EMAIL")
# for item in items:
#     print(f"{item[0]} {item[1]}:\t {item[2]}")

# c.execute("""--sql SELECT * FROM customers WHERE last_name LIKE 'Br%';""")
# items = c.fetchall()
# print("NAME \t\t EMAIL")
# for item in items:
#     print(f"{item[0]} {item[1]}:\t {item[2]}")

# c.execute("""--sql SELECT * FROM customers WHERE email LIKE '%codemy.com';""")
# items = c.fetchall()
# print("NAME \t\t EMAIL")
# for item in items:
#     print(f"{item[0]} {item[1]}:\t {item[2]}")


# Querying the database - ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC") # ASC is the default

c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

items = c.fetchall()
for item in items:
    print(item)
items = c.fetchall()
for item in items:
    print(item)



# Commit our command
connection.commit()


# Close our connection
connection.close()
