-- Vibha Murthy
-- SRN: PES1UG20CS495

CREATE TABLE Dance_School
(
  S_ID INT NOT NULL,
  Name VARCHAR(250) NOT NULL,
  Start_date DATE NOT NULL,
  Location VARCHAR(250) NOT NULL,
  PRIMARY KEY (S_ID)
);

CREATE TABLE Batch
(
  B_ID INT NOT NULL,
  Homework VARCHAR(500) NOT NULL,
  S_ID INT NOT NULL,
  PRIMARY KEY (B_ID),
  FOREIGN KEY (S_ID) REFERENCES Dance_School(S_ID)
);

CREATE TABLE Costume
(
  C_ID INT NOT NULL,
  Availability INT NOT NULL,
  Qty INT NOT NULL,
  Store VARCHAR(250) NOT NULL,
  PRIMARY KEY (C_ID)
);

CREATE TABLE Music_Band
(
  M_ID INT NOT NULL,
  Name VARCHAR(250) NOT NULL,
  PRIMARY KEY (M_ID)
);

CREATE TABLE Musician
(
  Mu_ID INT NOT NULL,
  Name VARCHAR(250) NOT NULL,
  Instrument VARCHAR(100) NOT NULL,
  M_ID INT NOT NULL,
  PRIMARY KEY (Mu_ID),
  FOREIGN KEY (M_ID) REFERENCES Music_Band(M_ID)
);

CREATE TABLE Dance_Style
(
  D_ID INT NOT NULL,
  Style VARCHAR(100) NOT NULL,
  PRIMARY KEY (D_ID)
);

CREATE TABLE Trainer
(
  T_ID INT NOT NULL,
  Name VARCHAR(250) NOT NULL,
  Phone_no LONG NOT NULL,
  D_ID INT NOT NULL,
  B_ID INT NOT NULL,
  PRIMARY KEY (T_ID),
  FOREIGN KEY (D_ID) REFERENCES Dance_Style(D_ID),
  FOREIGN KEY (B_ID) REFERENCES Batch(B_ID)
);

CREATE TABLE Performance
(
  P_ID INT NOT NULL,
  Venue VARCHAR(250) NOT NULL,
  Date DATE NOT NULL,
  Style INT NOT NULL,
  Song VARCHAR(250) NOT NULL,
  C_ID INT NOT NULL,
  M_ID INT NOT NULL,
  T_ID INT NOT NULL,
  PRIMARY KEY (P_ID),
  FOREIGN KEY (C_ID) REFERENCES Costume(C_ID),
  FOREIGN KEY (M_ID) REFERENCES Music_Band(M_ID),
  FOREIGN KEY (T_ID) REFERENCES Trainer(T_ID),
  FOREIGN KEY (Style) REFERENCES Dance_Style(D_ID)
);

CREATE TABLE Student
(
  Std_ID INT NOT NULL,
  F_name VARCHAR(250) NOT NULL,
  L_name VARCHAR(250) NOT NULL,
  Join_date DATE NOT NULL,
  Duration INT NOT NULL,
  DOB DATE NOT NULL,
  Address VARCHAR(500) NOT NULL,
  B_ID INT NOT NULL,
  P_ID INT,
  PRIMARY KEY (Std_ID),
  FOREIGN KEY (B_ID) REFERENCES Batch(B_ID),
  FOREIGN KEY (P_ID) REFERENCES Performance(P_ID)
);


INSERT INTO Music_Band VALUES (6000, "Venkatraman Troupe");
INSERT INTO Music_Band VALUES (6001, "Pineapple Express");
INSERT INTO Music_Band VALUES (6002, "Anova Ballet");
INSERT INTO Music_Band VALUES (6003, "Ramakrishna Musicians");
INSERT INTO Music_Band VALUES (6004, "Rock n Roll");

INSERT INTO Dance_School VALUES (1, "DanceOff", '2001-10-08', "Bangalore");
INSERT INTO Dance_School VALUES (2, "JustDanz", '2015-03-19', "Chennai");
INSERT INTO Dance_School VALUES (3, "Kalakshithi", '1966-08-06', "Bangalore");
INSERT INTO Dance_School VALUES (4, "NrutyaShala", '1992-01-29', "Delhi");

INSERT INTO Costume VALUES (7000, "Bharatanatyam Saree", "Y", 24, "Sri Costumes");
INSERT INTO Costume VALUES (7001, "Vesham", "Y", 12, "RMM Cotumes");
INSERT INTO Costume VALUES (7002, "Angivastra", "N", 0, "The Style Store");
INSERT INTO Costume VALUES (7003, "Leotard", "Y", 10, "The Style Store");
INSERT INTO Costume VALUES (7004, "Tutu", "Y", 15, "Ballet Things");
INSERT INTO Costume VALUES (7005, "Baggy pants", "Y", 40, "Sweep n Style");
INSERT INTO Costume VALUES (7006, "Sequined dressses", "Y", 10, "The Style Store");
INSERT INTO Costume VALUES (7007, "Passistas", "N", 0, "Sambamba");

INSERT INTO Dance_Style VALUES (5000, "Samba");
INSERT INTO Dance_Style VALUES (5001, "Salsa");
INSERT INTO Dance_Style VALUES (5002, "Western");
INSERT INTO Dance_Style VALUES (5003, "Hip Hop");
INSERT INTO Dance_Style VALUES (5004, "Freestyle");
INSERT INTO Dance_Style VALUES (5005, "Bharatanatyam");
INSERT INTO Dance_Style VALUES (5006, "Kuchupudi");
INSERT INTO Dance_Style VALUES (5007, "Kathakali");
INSERT INTO Dance_Style VALUES (5008, "Ballet");
INSERT INTO Dance_Style VALUES (5009, "Contemporary");
INSERT INTO Dance_Style VALUES (5010, "Break Dance");

LOAD DATA INFILE 'C:/Vibha Files/PES/Sem5/DBMS/Project/danceschooldata/batch.csv'
INTO TABLE Batch
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Vibha Files/PES/Sem5/DBMS/Project/danceschooldata/musician.csv'
INTO TABLE Musician
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Vibha Files/PES/Sem5/DBMS/Project/danceschooldata/trainer.csv'
INTO TABLE Trainer
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Vibha Files/PES/Sem5/DBMS/Project/danceschooldata/performance.csv'
INTO TABLE Performance
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Vibha Files/PES/Sem5/DBMS/Project/danceschooldata/student.csv'
INTO TABLE Student
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

--Trigger
DELIMITER $$
CREATE TRIGGER  check_age  BEFORE INSERT ON student
FOR EACH ROW
BEGIN
DECLARE d DATE;
DECLARE age INT;
SELECT SYSDATE() into d;
SET age = year(d) - year(NEW.dob);
IF age < 8 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'ERROR: 
         AGE MUST BE ATLEAST 8 YEARS!';
END IF;
END; $$
DELIMITER ;

-- Function 
DELIMITER $$
CREATE FUNCTION style (style_ID INT)
RETURNS INT
BEGIN
DECLARE cnt INT;
SELECT count(*) INTO CNT from Trainer where D_ID = style_ID group by D_ID;
RETURN cnt;
END; $$
DELIMITER ;

-- Procedure and Cursor
DELIMITER $$
CREATE procedure restock()
BEGIN 
    DECLARE done INT default 0;
    DECLARE cid int;
    DECLARE cost varchar(20);
    DECLARE avb varchar(2);
    DECLARE qty int;
    DECLARE store varchar(100);
    DECLARE tim_stm TIMESTAMP;
    DECLARE cur CURSOR FOR SELECT * FROM Costume;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cur;
    label: LOOP
    FETCH cur INTO cid, cost, avb, qty, store;
    IF avb = "N" THEN 
    UPDATE Costume SET availability = "Y", qty = 10 where availability = "N";
    END IF;
    IF done = 1 THEN LEAVE label;
    END IF;
    END LOOP;
    CLOSE cur;
   END$$
DELIMITER ;

update costume set availability = "N", qty = 0 where C_ID in (7002, 7007);

--Join
select p.P_ID, p.venue, p.Date, p.Style, p.Song, m.name, c.costume, c.availability, t.name, count(s.f_name) from 
(((performance as p natural join music_band as m) join costume as c on p.C_ID = c.C_ID) join trainer as t on p.T_ID = t.T_ID) join student as s on s.P_ID = p.P_ID group by p.P_ID;

--Aggregate
Select s.name, B_ID, count(*) from (student natural join batch) natural join dance_school as s group by name, B_ID;

--Set
SELECT D_ID FROM dance_style EXCEPT SELECT Style FROM performance;

--Change Implemented
DELIMITER $$
CREATE TRIGGER  check_batch_limit  BEFORE INSERT ON student
FOR EACH ROW
BEGIN
DECLARE bno int;
DECLARE tname varchar(50);
DECLARE msg varchar(250);
select name into tname from trainer where B_ID = new.B_ID limit 1;
set msg = concat('ERROR: Batch is Full! Please contact trainer for further details. Trainer name: ',tname);
SELECT count(*) into bno from student as s join batch as b on b.B_ID = s.B_ID where s.B_ID = new.B_ID;
IF bno > 20 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = msg;
END IF;
END; $$
DELIMITER ;

-- Custom query example
select mu.name, mu.instrument, m.name from musician as mu join music_band as m on m.M_ID = mu.M_ID;