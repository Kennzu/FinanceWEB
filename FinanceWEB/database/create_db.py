from dotenv import load_dotenv
import os
import asyncio
import asyncpg
import datetime
# import psycopg2

import sqlite3

# load_dotenv()

# async def main():
#     cur = await asyncpg.connect('postgresql://postgres:rqkTkovegEUKjsfOgpmmrYqpaFIgSEbY@postgres.railway.internal:5432/railway')
    
#     await cur.execute('''CREATE TABLE auth_info (
#                       id serial PRIMARY KEY,
#                       email TEXT NOT NULL,
#                       name TEXT NOT NULL,
#                       password TEXT NOT NULL
#                       )''')
    
#     await cur.execute('''INSERT INTO auth_info (email, name, password) VALUES(%s, %s, %s)''', ('kasha3365@yandex.ru', 'igor', 'aue13456'))
#     await cur.excecute('''SELECT * FROM auth_info''')

#     row = cur.fetchall()
#     print(row)
#     return row

# asyncio.run(main())


# db =  psycopg2.connect(dbname=(os.getenv('DBNAME')), user=(os.getenv('USER')), #Комп
#         password=(os.getenv('PASSWORD')), host=(os.getenv('HOST')), port=(os.getenv('PORT')))
# cur = db.cursor()

# cur.execute(f'''CREATE TABLE "{user}" (
#     id SERIAL NOT NULL PRIMARY KEY,
#     Категория TEXT,
#     Примечания TEXT,
#     ЗП_РС TEXT,
#     Размер INTEGER DEFAULT 0,
#     Карта_Нал TEXT,
#     time date NOT NULL
#     )''')

# db.commit()
# db.close()


db = sqlite3.connect('webDB.db')

cur = db.cursor()

# cur.execute('''CREATE TABLE auth_info (
#                       id INTEGER PRIMARY KEY,
#                       email TEXT NOT NULL,
#                       name TEXT NOT NULL,
#                       password TEXT NOT NULL
#                       )''')

cur.execute('''INSERT INTO auth_info (email, name, password) VALUES(?, ?, ?)''', ('kasha3365@yandex.ru', 'igor', '123456789'))

cur.execute('''SELECT * FROM auth_info''')

res = cur.fetchall()
print(res)