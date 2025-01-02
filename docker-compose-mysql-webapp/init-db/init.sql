CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100)  
);

INSERT INTO employees (name , role )
VALUES 
('Bar' , 'DevOps'),
('Gal' , 'Network Engineer'),
('Yaniv' , 'Junior Network Engineer');
