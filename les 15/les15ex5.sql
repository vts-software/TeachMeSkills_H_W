select a.first_name, a.last_name,
	sum(s.quantity) as total_sold
from authors a
join books b on b.author_id = a.id
join sales s on s.book_id = b.id
group by a.id, a.first_name, a.last_name
having sum(s.quantity) = (
	select max(total)
 	from (
   		select sum(s2.quantity) as total
   		from authors a2
   		join books b2 on b2.author_id = a2.id
   		join sales s2 on s2.book_id = b2.id
  		group by a2.id
	) as sub
);

select b.title,
	sum(s.quantity) as total_sold
from books b
join sales s on s.book_id = b.id
group by b.id, b.title
having sum(s.quantity) > (
	select avg(total)
	from (
		select sum(s2.quantity) as total
		from books b2
		join sales s2 on s2.book_id = b2.id
		group by b2.id
	) as sub
);