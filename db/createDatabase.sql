-- Active: 1686877706323@@127.0.0.1@3306
CREATE TABLE professional(
    id TEXT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    nome_social VARCHAR(100),
    created_at TEXT NOT NULL,
    updated_at TEXT
);


CREATE TABLE appointment(
    id TEXT PRIMARY KEY NOT NULL,
    professional_id TEXT NOT NULL,
    date TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT,

    Foreign Key (professional_id) REFERENCES professional(id)
);

INSERT INTO professional(id, nome, nome_social, created_at)
VALUES 
    ('5439b204-aa98-4f22-affb-e42b7fa60fcd', 'Marcia', '', DATETIME('now', 'localtime')),
    ('fad3a9de-1eba-41ea-a63b-b345731368d9', 'Fernando', 'Fernando', DATETIME('now', 'localtime')),
    ('d2ac6a0d-f7e5-453c-92c0-310fcfbaeadb', 'Fernando', 'Fernando', DATETIME('now', 'localtime'));

INSERT INTO appointment(id, professional_id, date, created_at)
VALUES 
    ('05d2bf3d-c278-4d13-9b16-df277d0b6fe7', '5439b204-aa98-4f22-affb-e42b7fa60fcd', '20/07/2023', DATETIME('now', 'localtime')),
    ('92fed857-997c-40b8-9f85-b811e1eabc9c', '5439b204-aa98-4f22-affb-e42b7fa60fcd', '25/07/2023', DATETIME('now', 'localtime')),
    ('8bb6836c-1a30-4042-8fc4-98749f9ba273', 'fad3a9de-1eba-41ea-a63b-b345731368d9', '21/07/2023', DATETIME('now', 'localtime')),
    ('6880e007-ebf4-4b7c-a96c-95dbb591e9d6', 'd2ac6a0d-f7e5-453c-92c0-310fcfbaeadb', '21/07/2023', DATETIME('now', 'localtime'));

SELECT * FROM professional;