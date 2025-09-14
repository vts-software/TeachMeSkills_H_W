
-- ex 3
select
a.first_name,
a.last_name,
b.title as book_title,
s.quantity
from authors a
inner join books b on b.author_id = a.id
inner join sales s on s.book_id = b.id

select
a.first_name,
a.last_name,
b.title as book_title,
s.quantity
from authors a
left join books b on b.author_id = a.id
left join sales s on s.book_id = b.id

-- ex 4
select
a.first_name,
a.last_name,
sum(s.quantity) as total_sold
from authors a
inner join books b on b.author_id = a.id
inner join sales s on s.book_id = b.id
group by a.id, a.first_name, a.last_name;

select
a.first_name,
a.last_name,
coalesce(sum(s.quantity)) as total_sold
from authors a
left join books b on b.author_id = a.id
left join sales s on s.book_id = b.id
group by a.id, a.first_name, a.last_name;
