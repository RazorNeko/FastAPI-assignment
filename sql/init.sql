CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description_short VARCHAR(255) NOT NULL,
    description_detail TEXT,
    status BOOLEAN DEFAULT FALSE,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
