# Django Todo List Application

A beginner-friendly Todo List web application built using **Python, Django, MySQL, Bootstrap 5.3, and Django REST Framework (DRF)**.

This project demonstrates CRUD operations, Django MVT architecture, REST API development, and database integration.

## Features

- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Manage task status
- Django REST API integration
- GET, POST, PUT, PATCH, DELETE methods
- JSON request and response handling
- Bootstrap responsive user interface
- MySQL database integration

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web application framework |
| MySQL | Database management |
| Django ORM | Database operations |
| Django REST Framework | REST API development |
| HTML5 | Web page structure |
| CSS3 | Web page styling |
| Bootstrap 5.3 | Responsive UI design |
| JavaScript | API requests using Fetch |
| JSON | API request and response format |

## Project Structure

```text
TodoList/
│
├── todolist/
│   ├── manage.py
│   │
│   ├── todolist/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── tasks/
│       ├── migrations/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│
├── venv/
├── .gitignore
├── requirements.txt
└── README.md
```

## Database Model

**Todo Model**

| Field | Type | Description |
|---|---|---|
| id | AutoField | Primary key |
| task | CharField | Task name |
| datetime | DateTimeField | Task date and time |
| status | CharField | Pending, In Progress, Completed |

## CRUD Operations

| HTTP Method | Operation | Description |
|---|---|---|
| GET | Read | Retrieve all tasks |
| POST | Create | Add a new task |
| PUT | Update | Update complete task data |
| PATCH | Partial Update | Update selected task fields |
| DELETE | Delete | Remove a task |

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/todos/` | Retrieve all tasks |
| POST | `/api/todos/add/` | Add a task |
| PUT/PATCH | `/api/todos/update/<id>/` | Update a task |
| DELETE | `/api/todos/delete/<id>/` | Delete a task |

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd task-application
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL database

Create a MySQL database and update the database configuration in `settings.py`.

### 7. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## Django Architecture

This project follows Django's MVT architecture.

- **Model:** Handles database structure and operations.
- **View:** Handles application logic and HTTP requests.
- **Template:** Displays the user interface using HTML and Bootstrap.

## Learning Objectives

- Understand Django MVT architecture.
- Learn Django ORM and MySQL integration.
- Implement CRUD operations.
- Understand REST API request and response.
- Work with HTTP methods and status codes.
- Use JavaScript Fetch API.
- Understand JSON data exchange.

## Future Improvements

- User registration and login authentication.
- Session and cookie management.
- User-specific todo tasks.
- API authentication and permissions.

## Author

Developed as a Python and Django learning project.