# Trackify – Bug Tracking System

A Django-based web application designed to help software development teams manage projects, report bugs, assign responsibilities, and track issue resolution.

## Overview

Trackify provides a centralized platform for organizing bug reports and monitoring their status throughout the development process. It includes user authentication, role-based access, project management, and bug tracking features.

## Features

- **User Authentication:** User registration and login.
- **Role-Based Access:** Different access levels for Admin, Developer, and Tester roles.
- **Dashboard:** Overview of bug counts and project status.
- **Project Management:** Create and manage projects.
- **Bug Reporting:** Submit bug reports with titles, descriptions, priorities, and status information.
- **Issue Tracking:** Monitor reported bugs and their resolution progress.
- **Comments:** Add comments to bug details for team communication.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Project Structure

```text
Trackify-Bug-Tracking-System/
├── manage.py
├── requirements.txt
├── bug_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tracker/
    ├── templates/
    ├── static/
    ├── views.py
    └── models.py
```

*Note: The structure above highlights the main application files and folders.*

## Getting Started

### Prerequisites

- Python 3
- pip
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LokeshKanojiya/Trackify-Bug-Tracking-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Trackify-Bug-Tracking-System
   ```

3. Create and activate a virtual environment.

   **Windows:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser:

   http://127.0.0.1:8000/

## Future Improvements

- Improve the user interface and dashboard experience.
- Add automated testing.
- Enhance deployment and production configuration.

## Author

**Lokesh Kanojiya**

- GitHub: [LokeshKanojiya](https://github.com/LokeshKanojiya)

---

*Trackify – Simplifying bug reporting and issue tracking for development teams.*
