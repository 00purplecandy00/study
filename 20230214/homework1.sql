-- 1
create table posts(
postId int not null auto_increment,
title varchar(50) not null,
content varchar(200) not null,
primary key(postId)
);

show columns from posts;

-- 2
alter table posts add(
writer varchar(100) not null default 'Anonymous',
created_at datetime not null  default now()
);

insert into posts (title,content) values('visit','myworld');
select * from posts;

show columns from posts;

-- 3
alter table posts change column content content text default null;

show columns from posts;

-- 4
alter table posts drop column writer;

show columns from posts;

-- 5
drop table posts;

show columns from posts;

-- 6
create table if not exists posts(
postId int not null auto_increment,
title varchar(50) not null null,
content text not null null,
writer varchar(20) not null null,
created_at datetime null null,
primary key(postId)
);

show columns from posts;

-- 7
drop table if exists posts;

show columns from posts;