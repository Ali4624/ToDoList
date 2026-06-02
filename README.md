# ✅ TodoList Console App

A lightweight command-line todo list application with persistent storage powered by a local **MySQL** database via the MySQL Connector.

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Database Setup](#database-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Branch Info](#branch-info)

---

## Features

- Create, read, update, and delete todo items from the console
- Persistent storage using a local MySQL database
- Simple and intuitive command-line interface
- Mark tasks as complete or pending
- View all tasks or filter by status

---

## Prerequisites

Before running the application, make sure you have the following installed:

- **MySQL Server** `8.0+` — [Download](https://dev.mysql.com/downloads/mysql/)
- **Python** `3.8+`
- **mysql-connector-python** `9.7.0`

> ⚠️ Make sure your MySQL service is running before launching the app.

---

## Database Setup

1. **Log in to MySQL:**
   ```bash
   mysql -u root -p
   ```

2. **Create the database and table:**
   ```sql
   CREATE DATABASE IF NOT EXISTS tododb;

   USE tododb;

   CREATE TABLE IF NOT EXISTS todos (
       id          INT AUTO_INCREMENT PRIMARY KEY,
       title       VARCHAR(255)    NOT NULL,
       description TEXT,
       is_done     BOOLEAN         NOT NULL DEFAULT FALSE,
       created_at  TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Create a dedicated user (recommended):**
   ```sql
   CREATE USER 'todouser'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON tododb.* TO 'todouser'@'localhost';
   FLUSH PRIVILEGES;
   ```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Switch to the MySQL branch:**
   ```bash
   git checkout feature/mysql-local-db
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies from `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt`:
   ```
   mysql-connector-python==9.7.0
   ```

---

## Configuration

Update the database connection settings in the config file (or `.env`):

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tododb
DB_USER=todouser
DB_PASSWORD=your_password
```

> 💡 Never commit credentials to version control. Add `.env` to your `.gitignore`.

---

## Usage

Run the application from the console:

```bash
python main.py
```

### Available Commands

| Command             | Description                        |
|---------------------|------------------------------------|
| `list`              | Show all todos                     |
| `list --pending`    | Show only incomplete tasks         |
| `list --done`       | Show only completed tasks          |
| `add "Task title"`  | Add a new todo item                |
| `done <id>`         | Mark a task as complete            |
| `undo <id>`         | Mark a task as incomplete          |
| `delete <id>`       | Delete a task                      |
| `clear`             | Delete all completed tasks         |
| `exit`              | Quit the application               |

---

## Project Structure

```
todolist-app/
├── main.py              # Entry point / main loop
├── db/
│   └── connection.py    # MySQL connector setup
├── models/
│   └── todo.py          # Todo model / data class
├── repository/
│   └── todo_repo.py     # CRUD operations via MySQL
├── .env.example         # Example environment config
├── .gitignore
└── README.md
```

---

## Branch Info

| Branch                   | Description                          |
|--------------------------|--------------------------------------|
| `main`                   | Stable release                       |
| `feature/mysql-local-db` | **This branch** — MySQL integration  |

This branch implements local database persistence using the MySQL Connector, replacing any previous in-memory or file-based storage.

---

## License

This project is licensed under the [MIT License](LICENSE).
