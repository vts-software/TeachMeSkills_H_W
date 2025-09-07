-- 1. Создаём таблицу Employees (Сотрудники)
CREATE TABLE Employees (
id serial primary key,
name VARCHAR(50),
Position VARCHAR(50),
Department VARCHAR(50),
Salary DECIMAL(10,2)
);


-- 2. Добавляем несколько сотрудников
INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('Иван Иванов', 'Developer', 'IT', 4000),
('Мария Петрова', 'Manager', 'Sales', 6000),
('Сергей Кузнецов', 'Analyst', 'Finance', 4500),
('Анна Смирнова', 'Developer', 'IT', 4200),
('Олег Орлов', 'Manager', 'HR', 5500);

-- 3. Обновляем данные (например, Сергей стал Senior Analyst)
UPDATE Employees
SET Position = 'Senior Analyst', Salary = 5000
WHERE Name = 'Сергей Кузнецов';

-- 4. Добавляем новое поле "HireDate" (дата приёма на работу)
ALTER TABLE Employees
ADD HireDate DATE;

-- 5. Заполняем даты приёма на работу
UPDATE Employees SET HireDate = '2020-05-10' WHERE Name = 'Иван Иванов';
UPDATE Employees SET HireDate = '2019-03-15' WHERE Name = 'Мария Петрова';
UPDATE Employees SET HireDate = '2021-07-01' WHERE Name = 'Сергей Кузнецов';
UPDATE Employees SET HireDate = '2022-01-20' WHERE Name = 'Анна Смирнова';
UPDATE Employees SET HireDate = '2018-11-30' WHERE Name = 'Олег Орлов';

-- 6. Найти всех сотрудников, у которых должность "Manager"
SELECT * FROM Employees
WHERE Position = 'Manager';

-- 7. Найти сотрудников с зарплатой больше 5000
SELECT * FROM Employees
WHERE Salary > 5000;

-- 8. Найти сотрудников из отдела "Sales"
SELECT * FROM Employees
WHERE Department = 'Sales';

-- 9. Средняя зарплата всех сотрудников
SELECT AVG(Salary) AS AverageSalary
FROM Employees;

-- 10. Удалить таблицу Employees
DROP TABLE Employees;
