SELECT p.payment,
       SUM(CASE WHEN c.customer_type = 'Member' THEN i.gross_income ELSE 0 END) AS member,
       SUM(CASE WHEN c.customer_type = 'Normal' THEN i.gross_income ELSE 0 END) AS normal
FROM invoice i
INNER JOIN payment p ON p.payment_id = i.payment_id
INNER JOIN customer c ON c.customer_id = i.customer_id
GROUP BY p.payment;