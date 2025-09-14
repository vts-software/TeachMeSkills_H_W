create table authors(
id serial primary key,
first_name varchar(55) not null,
last_name varchar(55) not null
);

create table books(
id serial primary key,
title varchar(255) not null,
author_id int not null,
foreign key (author_id) references authors(id),
publication_year smallint not null
);

create table sales(
id serial primary key,
book_id int not null,
foreign key (book_id) references books(id),
publication_year smallint not null
);
alter table sales
drop column publication_year;
alter table sales
add column quantity int not null check (quantity > 0);

insert into authors (first_name, last_name)
values
('Лев', 'Толстой'),
('Фёдор', 'Достоевский'),
('Александр', 'Пушкин');

insert into books (title, author_id, publication_year)
values
('Война и мир', 1, 1869),
('Преступление и наказание', 2, 1866),
('Евгений Онегин', 3, 1833);

insert into sales (book_id, quantity)
values
(1,10),
(2,20),
(3,30);
