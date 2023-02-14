create table examples (examId int auto_increment,lastName varchar(50) not null,firstName varchar(50) not null,primary key (examId));
show columns from examples;
-- drop table exmaples;


alter table  examples add(country varchar(100) not null);
alter table examples add(address varchar(100) not null,age varchar(20) not null);
alter table examples modify address varchar(50) not null;
alter table examples modify firstName varchar(10) not null, modify lastName varchar(10) not null;
alter table examples change column country state varchar(100) not null;
show columns from examples;
alter table examples drop column address;
show columns from examples;
alter table examples drop column state, drop column age;
show columns from examples;

create table articles (id int auto_increment, title varchar(100) not null, content varchar(200) not null,createdAt date not null, primary key(id));
insert into articles (title, content, createdAt) values('hello','world','2023-02-14');
insert into articles (title, content, createdAt) values('mytitle','mycontent',curdate());
insert into articles (title, content, createdAt) values('title1','content1','1900-01-01'),('title2','content2','2800-01-01'),('title3','content3','2800-01-01');

select * from articles;
update articles set title = 'newTitle' where id=1;
select * from articles;
update articles set content = replace(content,'content','test');
select * from articles;

delete from articles order by createdAt desc limit 2;