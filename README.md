# igor-associates

## Overview

**igor-associates** is a professional study project focused on building a web-based management system for law firms. The application is designed to manage lawyers, legal cases, and related workflows using a clean, modular, and scalable architecture.

The project is developed with **Python** and **Dash**, following real-world software engineering practices commonly used in professional environments.

---

## Project Goals

* Practice professional software architecture
* Apply modular design and separation of concerns
* Implement multi-page Dash applications
* Use version control with feature branches and pull requests
* Prepare the project for future scalability

---

## Tech Stack

* **Python 3.11+**
* **Dash**
* **Dash Bootstrap Components**
* **SQLite** (initial persistence layer)
* **uv** (dependency and environment management)
* **Git & GitHub** (version control)

---

## Project Structure

```text
igor-associates/
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── index.py
├── components/
│   ├── sidebar.py
│   └── home.py
├── modals/
│   └── modal_lawyers.py
├── services/
│   └── database.py
├── assets/
│   └── custom.css
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Architecture Overview

The project follows a clear separation of responsibilities:

* **app/**: Dash application instance and entry points
* **components/**: Reusable layout components
* **modals/**: UI modal dialogs (forms, confirmations)
* **services/**: Business logic and data access layer
* **assets/**: Static files (CSS, images)

This structure mirrors patterns used in production Dash applications.

---

## Running the Project (Development)

```bash
uv sync
uv run python app/index.py
```

---

## Version Control Workflow

This project uses a **branch-based workflow**:

* `main`: stable branch
* `feature/*`: new features and experiments

Each feature is developed in its own branch and merged via pull requests to simulate real-world team workflows.

---

## License

© 2026 Igor Associates. All rights reserved.

This repository is public for study and portfolio purposes.
Any use, reproduction, or distribution requires explicit permission from the author.

---

## Disclaimer

This project is intended for learning and professional development purposes. It is not production-ready softw
