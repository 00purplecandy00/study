-- 1
select employeeNumber,lastName,firstName,city
from employees
inner join offices
on employees.officeCode = offices.officeCode
order by employeeNumber asc;

-- 2
select customerNumber,officeCode,customers.city,offices.city
from customers
left join offices
on customers.city = offices.city
order by customerNumber desc;

-- 3
select customerNumber,officeCode,customers.city,offices.city
from customers
right join offices
on customers.city = offices.city
order by customerNumber desc;

-- 4
select customerNumber,officeCode,customers.city,offices.city
from customers
inner join offices
on customers.city = offices.city
order by customerNumber desc;

-- 5
-- 왼쪽집합을 집합A, 오른쪽 집합을 집합B라고 했을 떄,
-- left join(집합A, B집합에 없는 값은 null),
-- right join집합B, A집합에 없는 값은 null),
-- inner join(집합 A와 집합 B의 교집합)

-- 6
select customerNumber,officeCode,customers.city,offices.city
from customers
left join offices
on customers.city = offices.city
union
select customerNumber,officeCode,customers.city,offices.city
from customers
right join offices
on customers.city = offices.city
order by customerNumber desc;

-- 7
select orderdetails.orderNumber,orders.orderDate
from orderdetails
inner join orders
order by orderNumber asc;

-- 8
select orderNumber,orderdetails.productCode,productName
from orderdetails
inner join products
order by orderNumber asc;

-- 9
select orders.orderNumber,orderdetails.productCode, orderDate, productName
from orderdetails
inner join orders on orderdetails.orderNumber = orders.orderNumber
inner join products
order by orderNumber asc;