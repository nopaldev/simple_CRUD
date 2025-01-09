CREATE DATABASE flask_crud;

USE flask_crud;

CREATE TABLE mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(20) NOT NULL,
    nama VARCHAR(100) NOT NULL,
    asal VARCHAR(100) NOT NULL
);
