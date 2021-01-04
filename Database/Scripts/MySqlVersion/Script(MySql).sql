create Database if not exists DBKuppi;

USE DBKuppi;

CREATE TABLE Program(
	Pid int NOT NULL AUTO_INCREMENT,
	Name varchar(20) NOT NULL,
	CreditPoint float NOT NULL,
	YearCommenced date NOT NULL,
	CONSTRAINT PK_Program PRIMARY KEY(Pid) 
);

ALTER TABLE Program AUTO_INCREMENT=1;

CREATE TABLE Student(
	Stdid int NOT NULL AUTO_INCREMENT,
	Surname varchar(20) NOT NULL,
	GivenName varchar(20) NOT NULL,
	DoB date NOT NULL,
	YearEnrolled date NOT NULL,
	Pid int NOT NULL,
	CONSTRAINT PK_Student PRIMARY KEY(Stdid),
	CONSTRAINT FK_Student FOREIGN KEY(Pid) REFERENCES Program(Pid)
);

ALTER TABLE Student AUTO_INCREMENT=1;

CREATE TABLE Course(
	Cid int NOT NULL AUTO_INCREMENT,
	Name varchar(50) NOT NULL,
	CreditPoint float NOT NULL,
	YearCommenced date NOT NULL,
	Cyear int NOT NULL,
	Csem int NOT NULL,
	Pid int NOT NULL,
	CONSTRAINT PK_Course PRIMARY KEY(Cid),
	CONSTRAINT FK_Course FOREIGN KEY(Pid) REFERENCES Program(Pid)
);

ALTER TABLE Course AUTO_INCREMENT=1;

CREATE TABLE Attempt(
	Year int NOT NULL,
	Sem int NOT NULL,
	Mark int NOT NULL,
	Grade char NOT NULL,
	Stdid int NOT NULL,
	Cid int NOT NULL,
	CONSTRAINT PK_Attempt PRIMARY KEY(Year, Sem, Stdid, Cid),
	CONSTRAINT FK_AttemptStudent FOREIGN KEY(Stdid) REFERENCES Student(Stdid),
	CONSTRAINT FK_AttemptCourse FOREIGN KEY(Cid) REFERENCES Course(Cid)
);

INSERT INTO Program(name,creditpoint,yearcommenced) VALUES('IT', 50.0, '2000'); 
INSERT INTO Program(name,creditpoint,yearcommenced) VALUES('ITM', 50.0, '2000'); 

INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('Perera', 'Piumi', '0001', '2016', 1);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('Wickramasighe', 'Chiranga', '0001', '2016', 1);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('De Silva', 'Lahiru', '0001', '2016', 1);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('abc', 'abc', '0001', '2015', 2);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('xyz', 'xyz', '0001', '2014', 2);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('abc', 'abc', '0001', '2017', 1);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('xyz', 'xyz', '0001', '2017', 2);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('abc', 'abc', '0001', '2018', 2);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('xyz', 'xyz', '0001', '2018', 1);
INSERT INTO Student(surname,givenname,DoB,YearEnrolled,Pid) VALUES('abc', 'abc', '0001', '2014', 2);

INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Mathematics', 2.5, '2000', 4, 2, 1);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Programming', 4, '2000', 1, 2, 1);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('AI', 2.5, '2002', 3, 1, 1);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Accounting', 2.0, '2005', 2, 1, 1);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Database', 2.5, '2000', 1, 2, 1);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Multimedia', 2.5, '2005', 1, 2, 2);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Economics', 2.0, '2000', 2, 2, 2);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('EAD', 3, '2000', 3, 1, 2);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Marketing', 2.0, '2000', 2, 2, 2);
INSERT INTO Course(name,creditpoint,yearcommenced,Cyear,csem,pid) VALUES('Calculus', 4, '2000', 2, 1, 2);


INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(4, 2, 75, 'A', 1, 1);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(1, 2, 85, 'A', 2, 2);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(3, 1, 70, 'B', 3, 3);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(1, 2, 20, 'F', 4, 6);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 2, 75, 'C', 4, 6);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 1, 60, 'B', 5, 10);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 1, 45, 'C', 6, 4);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 2, 95, 'A', 7, 9);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 2, 78, 'A', 8, 9);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(1, 2, 23, 'F', 9, 5);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 2, 95, 'A', 10, 9);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(3, 1, 78, 'A', 10, 8);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 1, 67, 'B', 9, 4);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 1, 95, 'A', 2, 4);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 1, 12, 'F', 4, 10);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(3, 1, 23, 'F', 4, 10);
INSERT INTO Attempt(Year,Sem,Mark,Grade,Stdid,Cid) VALUES(2, 2, 50, 'C', 7, 7);


SELECT * FROM Attempt;
SELECT * FROM Course;
SELECT * FROM Program;
SELECT * FROM Student;

/* Drop Tables 

DROP TABLE Attempt;
DROP TABLE Course;
DROP TABLE Student;
DROP TABLE Program;
*/