CREATE DATABASE IF NOT EXISTS mydb;

USE mydb;

DROP TABLE IF EXISTS userlogin;

CREATE TABLE userlogin (
    userid INT PRIMARY KEY,
    username VARCHAR(30),
    userpassword VARCHAR(30)
);

INSERT INTO userlogin (userid, username, userpassword)
VALUES 
(1, 'dinesh', 'dinesh777'),
(2, 'santhosh', 'santhosh1707'),
(3, 'anbu', 'anbu0075');

SELECT * FROM userlogin;

UPDATE userlogin
SET userpassword = 'newpass123'
WHERE userid = 1;

SELECT * FROM userlogin
WHERE username = 'santhosh';

DELETE FROM userlogin
WHERE userid = 2;

--
SELECT * FROM userlogin;