
CREATE DATABASE cdoapi;

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255),
    token VARCHAR(255) UNIQUE
);

CREATE TABLE owners
(
    id SERIAL PRIMARY KEY,
    position_x INT,
    position_y INT,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE animals
( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    species VARCHAR(255) NOT NULL,
    owner INT,
    position_x INT,
    position_y INT,
    FOREIGN KEY (owner) REFERENCES owners (id)
);

-- username: demo, password: demo
INSERT INTO users (username, password) VALUES ('demo', '2a97516c354b68848cdbd8f54a226a0a55b21ed138e207ad6c5cbb9c00aa5aea');
INSERT INTO owners (name, position_x, position_y) VALUES
    ('alice', 5, 5),
    ('bertha', 20, 5),
    ('charlotte', 35, 5);
INSERT INTO animals (name, species, owner) VALUES
    ('tabby', 'cat', 1),
    ('luna', 'cat', 2),
    ('chloe', 'cat', 3),
    ('lily', 'dog', 1),
    ('sophie', 'dog', 2),
    ('lola', 'dog', 3);
