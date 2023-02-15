create table users(id int auto_increment, name varchar(50) not null, primary key(id));
create table articles(id int auto_increment, title varchar(50) not null,content varchar(100) not null, userId int not null,primary key(id));

insert into users(name) values('권미자'),('류준하'),('장영식');
insert into articles(title,content,userId) values('제목1','내용1',1),('제목2','내용2',2),('제목3','내용3',4);

select * from articles inner join users on articels.userId = users.id;
select articles.id,title,content,name from articles inner join users on articels.userId = users.id;

select productCode,productName,textDescription from products inner join productlines on products.productLine = productlines.productLine;