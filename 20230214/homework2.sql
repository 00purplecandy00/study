-- 1
create table users(
userId int not null auto_increment,
first_name varchar(20) not null,
last_name varchar(20) not null,
birthday date not null,
city varchar(100),
country varchar(100),
email varchar(100),
created_at datetime default now(),
primary key(userId)
);

drop table users;
show columns from users;

-- 2
insert into users (first_name,last_name,birthday,city,country,email) 
values
('Beemo','Jeong','1000-01-01',null,null,'beemo@hphk.kr'),
('Jieun','Lee','1993-05-16','Seoul','Korea',null),
('Dami','Kim','1995-04-09','Seoul','Korea',null),
('Kwangsoo','Lee','1985-07-14','Seoul','Korea',null)
;
select * from users;

-- 3
insert into users (first_name,last_name,birthday,city,country,email) 
values
('A','Jeong','1000-01-01',null,null,'beemo@hphk.kr'),
('B','Lee','1993-05-16','Seoul','Korea',null),
('C','Kim','1995-04-09','Seoul','Korea',null),
('D','Lee','1985-07-14','Seoul','Korea',null),
('E','Lee','1985-07-14','Seoul','Korea',null)
;

select * from users;
-- 4
update users set first_name = "Jeong eun" where userId = 2;
update users set last_name = "Seo" where userId = 2;
update users set birthday = "1988-10-22" where userId = 2;

-- 5
update users set country= ifnull("Korea","");

select * from users;

-- 6
delete from users where first_name='Beemo';


-- 7
delete from users where first_name = "Kwangsoo" and last_name = "Lee";

-- 8
delete from users order by created_at desc limit 1;