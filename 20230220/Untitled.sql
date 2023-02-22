drop table users;
set autocommit = 0;
create table users( id int auto_increment,name varchar(10) not null, primary key(id));

start transaction;

insert into users(name) values('harry'),('test');

select * from users;

-- rollback;

commit;

drop table articles;
create table articles
(id int auto_increment, 
title varchar(100) not null, 
createdAt datetime not null, 
updatedAt datetime not null, 
primary key(id));
insert into articles(title,createdAt, updatedAt) values('title1',current_time(),current_time());

select * from articles;

delimiter //
create trigger myTrigger
before update
on articles for each row
begin
set new.updatedAt = current_time();
end //
delimiter ;

show triggers;

update articles set title = 'newTitle' where id = 1;

create table articleLogs(id int auto_increment,description varchar(100) not null,createdAt datetime not null,primary key(id));


delimiter //
create trigger myTrigger2
after insert
on articles for each row
begin
insert into articleLogs(description,createdAt) values('글이 작성되었어요', current_date());
end //
delimiter ;

show triggers;

select * from articles;
select * from articleLogs;

update articles set title = 'title2' where id = 2;

delimiter //
create trigger myTrigger3
after insert
on articles for each row
begin
insert into articleLogs(description,createdAt) values(concat(new.id,'번 글이 작성되었어요',current_date());
end //
delimiter ;

show triggers;

select * from articles;
select * from articleLogs;

drop trigger myTrigger;
drop trigger myTrigger2;
drop trigger myTrigger3;

create table backupArticles
(id int auto_increment,
title varchar(100) not null,
createdAt datetime not null,
updatedAt datetime not null,
primary key(id));

delimiter //
create trigger myTrigger4
after delete
on articles for each row
begin
insert into backupArticles(title,createdAt,updatedAt) 
values(concat(old.title,old.current_time(),current_time()));
end//
delimiter ;

show triggers;
delete from articles where id = 1;

drop table backupArticles;
drop trigger myTrigger4;
select * from articles;
select * from backupArticles;
