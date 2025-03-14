
# 1

SELECT customerName, phone, city, country
FROM customers;

#2 
SELECT *
FROM customers
WHERE postalCode > 1370 OR salesRepEmployeeNumber > 150
LIMIT 10;

#3 
SELECT *
FROM customers
WHERE customerName LIKE '%Mini%'
LIMIT 10;

#4
SELECT *
FROM customers
WHERE state IN ('CA', 'NY')
LIMIT 10;

#5
SELECT *
FROM customers
WHERE creditLimit > 10000
LIMIT 10;
