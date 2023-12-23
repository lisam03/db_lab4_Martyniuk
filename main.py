import psycopg2

username = 'postgres'
password = '111'
database = 'f1'
host = 'localhost'
port = '5432'

"""
Перший запит
Вивести загальну суму балів, яку отримала кожна команда
"""
query_1 = '''
SELECT constructor_name, SUM(points) AS TotalPoints
	FROM constructors NATURAL JOIN results
GROUP BY constructor_name
ORDER BY TotalPoints ASC;
'''

"""
Другий запит
Вивести кількість пілотів кожної національності
"""
query_2 = '''
SELECT driver_nationality as Nationality, COUNT(driver_id) AS Total 
	FROM drivers
GROUP BY driver_nationality;
'''

"""
Третій запит
Вивести графік залежності балів від фінальної позиції, на яку приїхав пілот
"""
query_3 = '''
SELECT DISTINCT final_position as Position, points 
	FROM results
GROUP BY final_position, points
ORDER BY final_position;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")

    """
    Перший запит
    Вивести загальну суму балів, яку отримала кожна команда
    """
    print('1. ')
    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur.fetchall():
        print(row)

    """
    Другий запит
    Вивести кількість пілотів кожної національності
    """
    print('\n2.')
    cur = conn.cursor()
    cur.execute(query_2)
    for row in cur.fetchall():
        print(row)

    """
    Третій запит
    Вивести графік залежності балів від фінальної позиції, на яку приїхав пілот
    """
    print('\n3.')
    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur.fetchall():
        print(row)
