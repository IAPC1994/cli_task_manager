# CLI Task Manager 📝

A simple command-line **Task Manager** built in **Python**, featuring task persistence in JSON and unit tests.  
This project demonstrates Python fundamentals, modular design, and testing practices — perfect for learning Python and building a portfolio project.

---

## 🚀 Features

- Add, list, complete, and delete tasks
- Task status displayed with checkmarks (`✅`) or crosses (`❌`)
- Task persistence using JSON (`tasks.json`)
- Confirmation before deleting tasks
- Unit tests using `pytest`
- Structured as a professional Python package (`src/`)

---

## 🛠️ Technologies

- **Python 3.11+**
- **pytest** for testing
- **unittest.mock** for mocking inputs and file operations
- **JSON** for lightweight data persistence

---

## 📁 Project Structure

```
cli_task_manager/
├── src/
│ ├── init.py
│ ├── main.py
│ ├── task_manager.py
│ └── storage.py
├── tests/
│ └── test_task_manager.py
├── tasks.json (optional, ignored by git)
├── .gitignore
└── README.md
```

## ⚡ Usage

1. **Clone the repository**
2. ` cd cli_task_manager`
3. **Create venv:** `python -m venv venv`
4. **Activate venv:**

   1. Windows: `venv\Scripts\activate`
   2. Linux: `source venv/bin/activate`

5. Install dependencies: `pip install -r requirements.txt`
6. Run CLI: `python -m src.main`

7. Run tests: `pytest tests/`
