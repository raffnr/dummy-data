import mariadb
from products import generateData, get_id
from util import filter_space

keyword = input('Enter the products search keyword: ')
# Filtering keyword
keyword = filter_space(keyword)

pages = int(input('Enter the amount of the product pages: '))
categories = input('Enter products category: ')
id_num = get_id() + 1

insert_query = 'INSERT INTO products (id, name, category, price, stock) VALUES (%s, %s, %s, %s, %s)'

try:
    conn = mariadb.connect(
        user="root",
        host="localhost",
        port=3306,
        database="db_olshop"
    )
    cur = conn.cursor()

    data = generateData(keyword, pages, categories)

    succes = 0
    for i in range(len(data)):
        final_data = (f'SKU{id_num}', data[i][0], data[i][1], data[i][2], data[i][3])
        try:
            print(final_data)
            cur.execute(insert_query, final_data)
            conn.commit()
            id_num+=1
            succes+=1
        except mariadb.IntegrityError as e:
            if e.errno == 1062:
                print('error 1062')
                continue
            else:
                raise e
finally:
    print(f'Succesfully inserting {succes} data')
    # close connections
    cur.close()
    conn.close()