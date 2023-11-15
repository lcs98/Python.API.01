-- Apaga o banco de dados caso ele já exista.
-- DROP DATABASE IF EXISTS db_items;

-- cria o banco de dados com atenção á tabela de carecteres.
CREATE DATABASE db_items
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;
    
-- Selecionar o banco de dados.alter
USE db_items;
    
-- cria a tabela 'user' conforme o modelo.alter
CREATE TABLE user (
user_id INT PRIMARY KEY AUTO_INCREMENT,
user_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
user_name VARCHAR(127) NOT NULL,
user_email VARCHAR(255) NOT NULL,
user_password VARCHAR(63) NOT NULL,
user_birth DATE,
user_status ENUM('ON', 'OFF') DEFAULT 'on'
);

-- Insere dados em 'user'. 
INSERT INTO user (user_name, user_email, user_password, user_birth) VALUE 
('joca da silva','joca@dasilva.com','123','1980-12-14'),
('Marinelza sirlliano','mari@neuza.com','123','2000-08-09'),
('Setembrino trocatapas', 'set@tapas', '123', '1978-10-10');

-- Lista a inserção em 'user'. 
SELECT * FROM USER WHERE user_status = 'on' ORDER BY 'user_name';

-- Apaga o 'joca'. 
UPDATE user SET user_status = 'off' 	WHERE user_id = '1';

