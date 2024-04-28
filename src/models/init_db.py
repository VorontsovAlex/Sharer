# import psycopg2
import csv
import random
import pathlib
import os

import psycopg2


from src.models.const import CATEGORIES
from src.settings import settings

# conn = psycopg2.connect(settings.db_url)
#
# queries = [
# "insert into categories (name) values ('airplanes');",
# "insert into categories (name) values ('vaccum cleaners');",
# "insert into users (email, hashed_password, is_active) values ('123@123.ru', 'admin', True);",
#
#
# "insert into users (email, hashed_password, is_active) values ('user@oogle.com', 'user', True);",
# """
# insert into public.products (title,description,owner_id,category_id) values
# 	 ('airbus','brand new',1,1),
# 	 ('airbus 770','brand new',1,1),
# 	 ('dyson','brand new',1,2),
# 	 ('chinese shit','brand new',2,2);
# """
# ]
#
# def create_data():
#     conn = psycopg2.connect(settings.db_url)
#     create_categoties(conn)
#
#
# def create_categoties(conn, categories = CATEGORIES):
#     cursor = conn.cursor()
#
#     with open('../../source/products_with_categories.csv', mode='r') as file:
#         csvFile = csv.reader(file)
#         for lines in csvFile:
#             print(lines)
#
#     for category_id, category in categories.items():
#         query = f"insert into categories (id, name) values ({category_id}, '{category}');",
#         cursor.execute(query)
#
#
# def create_products(conn, categories = CATEGORIES):
#     cursor = conn.cursor()
#     pass


with open('./source/products_with_categories.csv', mode='r') as file:
    added_categories = dict()
    conn = psycopg2.connect(settings.db_url)
    cursor = conn.cursor()
    query = f"insert into users (id, email, hashed_password) values (1, 'admin@admin.ru', '123123');"
    cursor.execute(query)
    query = f"insert into users (id, email, hashed_password) values (2, 'admin2@admin.ru', '123123');"
    cursor.execute(query)
    query = f"insert into users (id, email, hashed_password) values (3, 'user@admin.ru', '123123');"
    cursor.execute(query)
    query = f"insert into users (id, email, hashed_password) values (4, 'user123@admin.ru', '123123');"
    cursor.execute(query)
    query = f"insert into users (id, email, hashed_password) values (5, 'user3@admin.ru', '123123');"
    cursor.execute(query)
    # conn.commit()
    # exit()

    csvFile = csv.reader(file)
    next(csvFile)
    for row in csvFile:
        title = row[1].replace("'", '')
        category_name = row[4].replace("'", '')
        file_name = row[2]
        img_full_path = os.path.join(os.getcwd(), 'source/images/', file_name)

        if category_name in added_categories:
            id_of_new_row = added_categories[category_name]
        else:
            query = f"insert into categories (id, name) values ({row[0]}, '{category_name}') RETURNING id;"
            cursor.execute(query)
            id_of_new_row = cursor.fetchone()[0]
            added_categories[category_name] = id_of_new_row

        try:
            query = (f"insert into products (id, title, owner_id, category_id, price_per_hour) "
                     f"values ({row[0]}, '{title}', {random.randint(1, 2)}, '{id_of_new_row}', {row[3]}) RETURNING id")
            cursor.execute(query)

            product_id = cursor.fetchone()[0]
        except Exception as exc:
            raise exc

        query = (f'insert into product_images (id, product_id, filename, file_path) '
                 f"values ({row[0]}, {product_id}, '{file_name}', '{img_full_path}')")
        cursor.execute(query)

    conn.commit()