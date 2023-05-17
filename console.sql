create database facesorce_app;

use facesorce_app;

create table client_info
(
    acount    char(18) not null,
    password  char(12) not null,
    telephone char(11) null,
    email     char(20) null
);

create table mark_data
(
    id   int         not null,
    mark varchar(10) not null
);

create table images
(
    id   int auto_increment
        primary key,
    data mediumblob null
);

create table notice_data
(
    author varchar(20)  not null,
    notice varchar(100) not null
);

create table admin
(
    acount char(18) not null primary key,
    password char(12) not null
);

insert into client_info(acount, password, telephone, email) VALUES ('abc','123456','12345678910','10086@qq.com');

insert into admin(acount, password) values('admin','123456');

insert into mark_data(id, mark) values(1,'12');