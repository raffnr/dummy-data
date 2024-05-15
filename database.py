import mariadb
import time
import math
from random_name import generate_instances

start_time = time.time()

data_amount = int(input('Masukan jumlah dummy data yang ingin digenerate: '))

data = []

index = 0

while index < data_amount:
    instances = generate_instances()

    if len(data) > 0:
        for i in range(len(data)):
            if data[i][0] == instances[0]:
                break
            elif i == (len(data) - 1):
                data.append(instances)
                index+=1
                print(f'inserting dummy data ke - {index}')
    else:
        data.append(instances)
        index+=1
        print(f'inserting dummy data ke - {index}')

insert_query = "INSERT INTO seller (email, first_name, last_name, city, phone) VALUES (%s, %s, %s, %s, %s)"

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
except mariadb.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close connections
    cur.close()
    conn.close()

end_time = time.time()
total_time = end_time - start_time
print(f'Berhasil inserting {index} dummy data ke database dalam waktu {math.floor(total_time)} detik')
