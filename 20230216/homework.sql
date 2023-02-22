-- 1
select productCode,productName,MSRP from products where MSRP > (select avg(MSRP) from products) order by MSRP asc;

-- 2
select distinct customers.customerNumber,customers.customerName 
from customers join orders using (customerNumber)
where orderDate > "2003-01-06" and orderDate < "2003-03-26"
order by customerNumber asc;

-- 3
select productCode,productName,productLine,MSRP
from products
where productLine = "Classic Cars" and MSRP = (select max(MSRP) from products);

-- 4

-- 5

-- 6