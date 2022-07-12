SELECT order_id,
	   b.customer_id,
	   customer_city,
	   order_purchase_timestamp 
FROM tb_order AS a
	LEFT JOIN tb_customer AS b ON a.customer_id = b.customer_id 
WHERE order_status NOT LIKE '%canceled%' 