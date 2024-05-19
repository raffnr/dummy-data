import mariadb
from products import generateData
from util import filter_space

db_name = input('Enter database name: ')
keyword = input('Enter the products search keyword: ')
# Filtering keyword
keyword = filter_space(keyword)

pages = int(input('Enter the amount of the product pages: '))
categories = input('Enter products category: ')

insert_query = 'INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)'

try:
    conn = mariadb.connect(
        user="root",
        host="localhost",
        port=3306,
        database=db_name
    )
    cur = conn.cursor()

    data = generateData(keyword, pages, categories)

    succes = 0
    for i in range(len(data)): 
        try:
            cur.execute(insert_query, data[i])
            conn.commit()
            succes+=1
        except mariadb.IntegrityError as e:
            if e.errno == 1062:
                continue 
            else:
                raise e
finally:
    print(f'Succesfully inserting {succes} data')
    # close connections
    cur.close()
    conn.close()