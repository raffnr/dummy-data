import mariadb
from random_name import generate_instances

data_amount = int(input('Enter number of data that you want to generate: '))

data = []

for i in range(data_amount):
    data.append(generate_instances())

insert_query = "INSERT INTO seller (email, first_name, last_name, phone) VALUES (%s, %s, %s, %s)"

try:
    conn = mariadb.connect(
        user="root",
        host="localhost",
        port=3306,
        database="latihan_mysql"
    )
    cur = conn.cursor()

    # Execute the query with data
    cur.executemany(insert_query, data)

    # Commit the changes to the database
    conn.commit()
    print("Data berhasil di insert ke database!")
except mariadb.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close connections
    cur.close()
    conn.close()

