import mariadb
import time
import math
from random_name import generate_instances


data_amount = int(input('Masukan jumlah dummy data yang ingin digenerate: '))

t = time.time()

insert_query = "INSERT INTO seller (email, first_name, last_name, city, phone) VALUES (%s, %s, %s, %s, %s)"

try:
    conn = mariadb.connect(
        user="root",
        host="localhost",
        port=3306,
        database="latihan_mysql"
    )
    cur = conn.cursor()

    i = 0 # index

    while i < data_amount: 
        # Generate dummy data
        data = generate_instances() # Note for myself: add more condition in this func for generating fake emails

        try:
            cur.execute(insert_query, data)
            conn.commit()
            i+=1 # dieksekusi jika query berhasil
            # print(f"Inserting data ke-{i}")
        except mariadb.IntegrityError as e:
            # cek error duplicate PK kode 1062
            if e.errno == 1062:
                continue # error 1062 continue loop tanpa increment index untuk generate data berikutnya
            # Jika error selain 1062 maka loop berhenti
            else:
                raise e  # loop berhenti raise error diluar loop
finally:
    # close connections
    cur.close()
    conn.close()
    end_time = time.time()
    total_time = end_time - t
    print(f'Berhasil inserting {i} data ke database dalam waktu {math.floor(total_time)} detik')