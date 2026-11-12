--  Se o database existe (apagar)
DROP DATABASE IF EXISTS estudolist;

-- Criando o database
CREATE DATABASE estudolist;

-- Colocando o database em uso
USE estudolist;

-- Criando a tabela (tarefa)
CREATE TABLE tarefa(
    idTarefa INT PRIMARY KEY AUTO_INCREMENT,
    nomeTarefa VARCHAR(30) NOT NULL,
    descricao VARCHAR(100),
    categoria VARCHAR(30) NOT NULL,
    dataPrazo DATE NOT NULL,
    prioridade ENUM('ALTA','MEDIA','BAIXA') NOT NULL,
    status ENUM('Pendente','Concluída','Não realizada') DEFAULT "Pendente"
); 