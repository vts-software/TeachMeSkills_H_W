-- 1. Создаём таблицу Employees (Сотрудники)
create table employees (
id serial primary key,
name varchar(50),
position varchar(50),
department varchar(50),
salary decimal(10,2)
);


-- 2. Добавляем несколько сотрудников
insert into employees (name, position, department, salary)
values
('Иван Иванов', 'Developer', 'IT', 4000),
('Мария Петрова', 'Manager', 'Sales', 6000),
('Сергей Кузнецов', 'Analyst', 'Finance', 4500),
('Анна Смирнова', 'Developer', 'IT', 4200),
('Олег Орлов', 'Manager', 'HR', 5500);

-- 3. Обновляем данные (например, Сергей стал Senior Analyst)
update employees
set position = 'Senior Analyst', salary = 5000
where name = 'Сергей Кузнецов';

-- 4. Добавляем новое поле "HireDate" (дата приёма на работу)
alter table employees
add hire_date date;

-- 5. Заполняем даты приёма на работу
update employees set hire_date = '2020-05-10' where name = 'Иван Иванов';
update employees set hire_date = '2019-03-15' where name = 'Мария Петрова';
update employees set hire_date = '2021-07-01' where name = 'Сергей Кузнецов';
update employees set hire_date = '2022-01-20' where name = 'Анна Смирнова';
update employees set hire_date = '2018-11-30' where name = 'Олег Орлов';

-- 6. Найти всех сотрудников, у которых должность "Manager"
select * from employees
where position = 'Manager';

-- 7. Найти сотрудников с зарплатой больше 5000
select * from employees
where salary > 5000;

-- 8. Найти сотрудников из отдела "Sales"
select * from employees
where department = 'Sales';

-- 9. Средняя зарплата всех сотрудников
select avg(salary) as average_salary
from Employees;

-- 10. Удалить таблицу Employees
drop table employees;
