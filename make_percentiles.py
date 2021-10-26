SELECT CategoryID, (total/t2.cnt)*100 AS 퍼센트
FROM (
		SELECT CategoryID, SUM(Price) AS total
		FROM Products
		GROUP BY CategoryID
	 ) AS t1, 
     (
     	SELECT sum(Price) AS cnt
		FROM Products
    ) AS  t2
GROUP BY CategoryID
ORDER BY CategoryID ASC
