import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '111'
database = 'f1'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT constructor_name, SUM(points) AS TotalPoints
	FROM constructors NATURAL JOIN results
GROUP BY constructor_name
ORDER BY TotalPoints ASC;
'''

query_2 = '''
SELECT driver_nationality as Nationality, COUNT(driver_id) AS Total 
	FROM drivers
GROUP BY driver_nationality;
'''

query_3 = '''
SELECT DISTINCT final_position as Position, points 
	FROM results
GROUP BY final_position, points
ORDER BY final_position;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(15, 5))

    """
    Перший запит
    Вивести загальну суму балів, яку отримала кожна команда
    """
    cur.execute(query_1)
    constructors = []
    total = []

    for row in cur:
        constructors.append(row[0])
        total.append(row[1])

    x_range = range(len(constructors))

    bar_ax.bar(x_range, total, label='Total')
    bar_ax.set_title('Загальна сума балів, яку отримала кожна команда')
    bar_ax.set_xlabel('Команди')
    bar_ax.set_ylabel('Сума балів')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(constructors)
    bar_ax.legend()

    """
    Другий запит
    Вивести кількість пілотів кожної національності
    """
    cur.execute(query_2)
    driver_nationality = []
    total = []

    for row in cur:
        driver_nationality.append(row[0])
        total.append(row[1])

    pie_ax.pie(total, labels=driver_nationality, autopct='%1.1f%%')
    pie_ax.set_title('Кількість пілотів кожної національності')
    #pie_ax.legend()
    # легенда до кругової діаграми

    """
    Третій запит
    Вивести графік залежності балів від фінальної позиції, на яку приїхав пілот
    """
    cur.execute(query_3)
    position = []
    points = []

    for row in cur:
        position.append(row[0])
        points.append(row[1])

    graph_ax.plot(position, points, marker='o')
    graph_ax.set_xlabel('Позиція')
    graph_ax.set_ylabel('Кількість балів')
    graph_ax.set_title('Графік залежності балів від фінальної позиції, на яку приїхав пілот')

    for qnt, price in zip(position, points):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')

plt.tight_layout()
plt.show()
