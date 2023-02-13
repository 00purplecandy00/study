-- 1
select distinct country
from customers
order by country asc;

-- 2
select distinct state
from custromers
order by state desc;

-- 3
select customerNumber, customerName, country
from customers
where country != 'USA'
order by customerNumber desc;

-- 4
select *
from offices
where city = 'Paris';

-- 5
select customerNumber, customerName, country, state
from customers
where country = 'USA' and state = 'CA'
order by customerName desc;

-- 6
select customerNumber,customerName,country,state
from customers
where country='USA' and (state='CA' or state = 'NY')
order by customerNumber desc;

-- 7
select customerNumber,customername,state
from customers
where state in ('CA','NY','CT','PA')
order by customerNumber desc;

-- 8
select productCode,productName,quantityInStock
from products
where quantityInStock < 1000
order by quantityInStock asc;

-- 9
select productCode,productName,quantityInStock
from products
where quantityInStock > 2000 and quantityInStock < 3000
order by quantityInStock desc;

-- 10
select customerNumber,customerName,phone
from customers
where phone like '%555'
order by customerName desc;

-- 11
select productCode, quantityInStock
from products
order by quantityInStock desc
limit 5;

-- 12
select jobTitle,count(jobTitle)
from employees
group by jobTitle
order by count(jobTItle) desc, jobTitle desc;

-- 13
select country,count(country)
from customers
group by country
order by count(country) desc, country desc;

-- 14
select orderNumber,sum(quantityOrdered * priceEach) as total
from orderdetails
group by orderNumber
order by sum(quantityOrdered * priceEach) desc;

-- 15
select year(orderDate),count(orderNumber)
from orders
group by year(orderDate);

-- 16
select productLine,max(quantityInStock) as max_stock
from products
where quantityInStock < 9000
group by productLine;

-- 17
select orderNumber,sum(quantityOrdered) as itemsCount,sum(priceEach*quantityOrdered) as total
from orderdetails
group by orderNumber
having sum(quantityOrdered) >= 500 and sum(priceEach*quantityOrdered) >= 50000;