insert into authors (first_name, last_name)
values 
('Николай', 'Гоголь'),
('Иван', 'Тургенев'),
('Антон', 'Чехов'),
('Максим', 'Горький'),
('Сергей', 'Есенин'),
('Владимир', 'Маяковский'),
('Марина', 'Цветаева'),
('Александр', 'Блок'),
('Михаил', 'Булгаков'),
('Борис', 'Пастернак');

insert into books (title, author_id, publication_year)
values 
('Мёртвые души', 14, 1842),
('Отцы и дети', 15, 1862),
('Мастер и Маргарита', 22, 1967),
('Доктор Живаго', 23, 1957); 


select b.title as book_title,
a.first_name,
a.last_name
from books b
inner join authors a on b.author_id = a.id

select b.title as book_title,
a.first_name,
a.last_name
from authors a
left join books b on b.author_id = a.id;

select b.title as book_title,
a.first_name,
a.last_name
from books b
right join authors a on b.author_id = a.id;
