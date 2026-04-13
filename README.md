# ⚡️ TaskMaster CLI
### *Manage your chaos from the terminal.*

---

`TaskMaster` is a lightweight, high-performance command-line interface designed for developers who live in the terminal and find traditional GUIs... *distracting*. No fluff, no electron bloat—just you, your tasks, and the prompt.

---

## 🚀 Quick Start

Get up and running in seconds:

```bash
# Install via npm
npm install -g taskmaster-cli

# Or clone and build
git clone https://github.com/username/taskmaster.git
cd taskmaster && make install
```

---

## 🛠 Usage & Syntax

TaskMaster uses intuitive, single-letter aliases to keep your fingers on the home row.

| Command | Alias | Description |
| :--- | :--- | :--- |
| `task add "Buy milk"` | `a` | Create a new entry |
| `task list` | `ls` | Show all pending tasks |
| `task done 1` | `d` | Mark task #1 as complete |
| `task delete 3` | `rm` | Remove task #3 forever |
| `task priority 2 high` | `p` | Set priority level |

---

## ✨ Features

* **Offline First:** Your data stays on your machine in a simple `.json` or `.sqlite` store.
* **Color Coded:** Visual cues for priorities (🔴 High, 🟡 Medium, 🔵 Low).
* **Smart Parsing:** Supports hashtags for categorization (e.g., `task add "Fix bug #work"`).
* **Lightning Fast:** Written in [Language, e.g., Rust/Go], it cold-starts in under 10ms.

---

## ⚙️ Configuration

Customize your experience by editing `~/.taskmasterrc`.

```json
{
  "theme": "dracula",
  "default_priority": "medium",
  "auto_cleanup": true,
  "date_format": "YYYY-MM-DD"
}
```

---

## 🤝 Contributing

Got a feature idea or found a bug? We love PRs! 

1.  **Fork** the project.
2.  **Create** your feature branch: `git checkout -b feature/AmazingFeature`.
3.  **Commit** your changes: `git commit -m 'Add some AmazingFeature'`.
4.  **Push** to the branch: `git push origin feature/AmazingFeature`.
5.  **Open** a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

> *“The shortest way to do many things is to only do one thing at a time.”*