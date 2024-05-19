import requests
import mariadb
from bs4 import BeautifulSoup
import random

def get_id():
    conn = mariadb.connect(
        user="root",
        host="localhost",
        port=3306,
        database="db_olshop"
    )
    cur = conn.cursor()

    cur.execute("SELECT COUNT(name) FROM products")
    conn.commit()

    for i in cur:
        data = i

    conn.close()
    return data[0]

def generateData(search_key, num_pages, category):
    data = []
    for i in range(num_pages):
        r = requests.get(f'https://www.klikindomaret.com/search/?key={search_key}&page={i + 1}')

        html_content = f'{r.text}'

        html_document = BeautifulSoup(html_content, 'html.parser')

        title = html_document.css.select(".title")
        price = html_document.css.select(".price-value")
        
        j = 3

        while j < len(title) - 33:
            produk = title[j].string[1:]
            harga_raw = price[j - 3].string[3:].split('.')
            harga = harga_raw[0] + harga_raw[1]
            stock = random.randint(50, 300)
            data_tuple = (produk, category, int(harga), stock)
            data.append(data_tuple)
            j+=1
    
    return data


