USE DBKuppi;

-- Creating the Table
CREATE TABLE if not exists Admin(
	Aid int NOT NULL AUTO_INCREMENT,
	Name varchar(40),
	Pid int NOT NULL,
	Status varchar(40) DEFAULT 'Active',
	CONSTRAINT PK_Admin PRIMARY KEY(Aid),
	CONSTRAINT FK_Admin FOREIGN KEY(Pid) REFERENCES Program(Pid)
);

-- Select, Update, Delete and Insert into table
INSERT INTO Admin(Name,Pid,Status) VALUES('Piumi', 1, DEFAULT);
INSERT INTO Admin(Name,Pid,Status) VALUES('Chiranga', 2, DEFAULT);

SELECT * FROM Admin;

UPDATE Admin SET Name = 'abc' WHERE Aid = 1;
DELETE FROM Admin WHERE Aid =2;

-- Alter table
ALTER TABLE Admin
MODIFY COLUMN Name varchar(40) NOT NULL;

-- Select queries
SELECT * FROM Program
WHERE Name = 'IT';

SELECT Stdid, Surname, GivenName 
FROM Student;

SELECT  DISTINCT GivenName FROM Student;

SELECT * FROM Course 
WHERE Name LIKE '[e,a]%';

SELECT * FROM Attempt
ORDER BY Mark DESC;

SELECT * FROM Attempt a 
WHERE a.Mark > 70
ORDER BY Mark;

-- Joins
SELECT *
FROM Student s
INNER JOIN Attempt a
ON s.Stdid = a.Stdid;

SELECT * 
FROM Student s, Attempt a
WHERE s.Stdid = a.Stdid;

SELECT s.GivenName, a.Mark
FROM Student s
INNER JOIN Attempt a ON s.Stdid = a.Stdid
INNER JOIN Course c ON a.Cid = c.Cid
WHERE a.Mark>50 
AND c.Name = 'Calculus';

SELECT s.stdid, s.GivenName, s.Surname, a.Mark
FROM Student s
LEFT OUTER JOIN Attempt a ON s.Stdid = a.Stdid;

SELECT s.stdid, s.GivenName, s.Surname, a.Mark
FROM Student s
RIGHT OUTER JOIN Attempt a ON s.Stdid = a.Stdid;

-- Aggregates
SELECT COUNT(DISTINCT Stdid) AS Number_of_Students
FROM Attempt
WHERE Mark>50;

SELECT DISTINCT Stdid FROM Attempt WHERE Mark>50;

SELECT MAX(a.Mark)
FROM Student s, Attempt a, Course c
WHERE s.Stdid = a.Stdid
AND a.Cid = c.Cid
AND c.Name = 'Accounting';

SELECT MIN(a.Mark)
FROM Attempt a, Course c
WHERE a.Cid = c.Cid
AND c.Name = 'Accounting';

SELECT AVG(a.Mark)
FROM Attempt a, Course c
WHERE a.Cid = c.Cid
AND c.Name = 'Calculus';

SELECT SUM(Mark)
FROM Attempt;


