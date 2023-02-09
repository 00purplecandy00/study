##1

select
	*
from
	employees;
    
##2
select
	customerNumber,
    customerName,
    phone
from
	customers;
    
##3
select
	firstName,
    lastName,
    email
from
	employees
order by
	firstName asc;
    
##4
select
	firstName as '이름',
	lastName as '성',
    email as '이메일'
from
	employees
order by
    '이름' asc;
    
##5
select
	employeeNumber,
    lastName,
    firstName,
    officeCode,
    jobTitle
from
	employees
order by
	jobTitle desc,
    officeCode desc;
    
##6
select
	*
from
	orderdetails
order by
	quantityOrdered asc,
    priceEach asc;

##7
select
	customerNumber,
    country,
    contactFirstname
from
	customers
order by
	country asc,
    contactFirstName desc;
    
##8
select
	productCode,
    quantityInStock,
    buyPrice,
    quantityInStock * buyPrice
from
	products
order by
	quantityInStock * buyPrice desc;