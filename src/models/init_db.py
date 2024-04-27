import psycopg2

from src.settings import settings

conn = psycopg2.connect(settings.db_url)

queries = [
"insert into categories (name) values ('airplanes');",
"insert into categories (name) values ('vaccum cleaners');",
"insert into users (email, hashed_password, is_active) values ('123@123.ru', 'admin', True);",


"insert into users (email, hashed_password, is_active) values ('user@oogle.com', 'user', True);",
"""
insert into public.products (title,description,owner_id,category_id) values
	 ('airbus','brand new',1,1),
	 ('airbus 770','brand new',1,1),
	 ('dyson','brand new',1,2),
	 ('chinese shit','brand new',2,2);
"""
]

def create_data():
    for query in queries:
        conn.execute(query)
