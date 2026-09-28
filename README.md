# Bug Tracking System

A full-stack Django web application designed for software development teams to track projects and effectively report, assign, and resolve bug tickets.

## Features

- **User Authentication & Roles**: Sign up, log in, and utilize role-based access control (Admin, Developer, Tester).
- **Dashboard Overview**: Monitor total, open, and resolved bug counts along with project statuses.
- **Project Management**: Create projects (Admins) and monitor their tickets.
- **Bug Reporting**: Submit tickets containing titles, descriptions, priorities, screenshots, and statuses.
- **Comments**: Post comments on bug details pages.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher

### Installation & Setup

1. **Activate the Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install django pillow
   ```

3. **Apply Database Migrations**:
   The project is pre-configured with SQLite. Run migrations to initialize the database:
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser**:
   Create an admin account to access the full capabilities of the system.
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser.

## Tech Stack
- **Backend**: Python, Django
- **Frontend**: HTML5, Bootstrap 5 UI, CSS
- **Database**: SQLite
