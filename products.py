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

        # Why j start from 3? because the variable title will generate array in form of somethimg like this
        # [
        # <div>Not title</div>  index 0
        # <div>Not title</div>  index 1    
        # <div>Not title</div>  index 2
        # <div>Title</div>      index 3 so the title only start from index 3
        # <div>Title</div>
        # <div>Title</div>
        # ]

        while j < len(title) - 33:
            # Get product name
            produk = title[j].string[1:]

            # Filtering price
            harga_raw = price[j - 3].string[3:]
            dot = 0
            for char in harga_raw:
                if char == '.':
                    dot+=1
                    break
            
            if dot > 0:
                harga_raw = harga_raw.split('.')
                harga = harga_raw[0] + harga_raw[1]
            else:
                harga = harga_raw
            
            # Generating random stock
            stock = random.randint(50, 300)

            # Merge all value to a sigle array
            data_arr = [produk, category, int(harga), stock]
            data.append(data_arr)
            j+=1
    
    return data



