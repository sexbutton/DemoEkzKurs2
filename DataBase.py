import psycopg2

# Установка соединения с базой данных
conn = psycopg2.connect(
    host='localhost',
    database='DemoEkz',
    user='postgres',
    password='GAVNO007'
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Пример выполнения SQL-запроса
cur.execute("SELECT * FROM demoekz")

# Получение результатов запроса
rows = cur.fetchall()

print(rows)

# Закрытие курсора и соединения
cur.close()
conn.close()