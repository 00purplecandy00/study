select customerNumber from payments where amount = (select max(amount) from payments);

select * from employees;
select * from offices;

select lastName,firstName from employees where officeCode in (select officeCode from offices where country = "USA");

select customerName from customers where customerNumber not in (select customerNumber from orders);

select * from customers;
select * from payments;

select customerNumber, amount, contactFirstName 
from (select * from payments inner join customers using (customerNumber)) as mySub 
where amount = (select max(amount) from payments);

select customerNumber,customerName from customers 
where exists (select * from orders where customers.customerNumber = orders.customerNumber);

select employeeNumber,firstName,lastName from employees
where exists (select * from offices where city = "Paris" and employees.officeCode = offices.officeCode);

select contactFirsttName, creditLimit, 
case when creditLimit > 100000 then "VIP" when creditLimit > 70000 then "Platinum" else "Bronze"
end as grade
from customers;

select orderNumber,status,
case when status="In Process" then "주문중" when status="shipped" then "발주완료" when status="Cancelled" then "주문취소" else "기타사유"
end as details
from orders;