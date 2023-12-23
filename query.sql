--Вивести загальну суму балів, яку отримала кожна команда
SELECT constructor_name, SUM(points) AS TotalPoints
	FROM constructors NATURAL JOIN results
GROUP BY constructor_name
ORDER BY TotalPoints ASC;

--Вивести кількість пілотів кожної національності
SELECT driver_nationality as Nationality, COUNT(driver_id) AS Total 
	FROM drivers
GROUP BY driver_nationality;

--Вивести залежність балів від фінальної позиції, на яку приїхав пілот
SELECT DISTINCT final_position as Position, points 
	FROM results
GROUP BY final_position, points
ORDER BY final_position;
