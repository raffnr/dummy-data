import mariadb
from random_name import generate_instances

data = []

for i in range(100):
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
    print("Data inserted successfully!")
except mariadb.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close connections
    cur.close()
    conn.close()

