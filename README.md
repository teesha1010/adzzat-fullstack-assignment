# adzzat-fullstack-assignment

The project includes two benchmark-style coding tasks, automated test graders, Docker-based execution environments, and a web interface to browse task descriptions and difficulty levels.

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | Next.js |
| Language | JavaScript |
| Backend | Python, Django |
| API | Django REST Framework |
| Testing | Pytest |
| Containerization | Docker |
| Version Control | Git and GitHub |

## Project Structure

```text
adzzat-fullstack-assignment/
│
├── tasks/
│   ├── task-1-calculator/
│   │   ├── app.py
│   │   ├── task.md
│   │   ├── Dockerfile
│   │   ├── grader/
│   │   │   └── test_task.py
│   │   └── solution/
│   │       └── app.py
│   │
│   └── task-2-registration/
│       ├── app.py
│       ├── task.md
│       ├── Dockerfile
│       └── grader/
│           └── test_task.py
│
├── backend/
│   ├── config/
│   ├── api/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   └── app/
│   │       ├── globals.css
│   │       ├── layout.js
│   │       └── page.js
│   └── package.json
│
├── README.md
└── NOTES.md
```


## Coding Tasks

### Task 1: Python Calculator

- **Type:** Language-driven
- **Difficulty:** Easy
- **Environment:** Python 3.11, Ubuntu, Pytest

This task requires fixing a Python calculator implementation.

Requirements:
- Implement addition, subtraction and multiplication correctly.
- Support decimal division.
- Raise `ZeroDivisionError` when dividing by zero.

The automated grader checks normal calculations, decimal division and division-by-zero handling.

### Task 2: User Registration

- **Type:** Outcome-driven
- **Difficulty:** Medium
- **Environment:** Python 3.11, Ubuntu, Pytest

This task requires improving a user registration function.

Requirements:
- Accept valid email addresses.
- Reject invalid email addresses.
- Prevent duplicate registrations.
- Handle email addresses case-insensitively.
- Remove unnecessary leading and trailing spaces.
- Return appropriate success and error responses.

The automated grader checks registration behaviour and edge cases.

## Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.11 or later
- Node.js and npm
- Docker Desktop
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/teesha1010/adzzat-fullstack-assignment.git
cd adzzat-fullstack-assignment
```

### 2. Backend Setup – Django

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

Backend runs at:

`http://127.0.0.1:8000/`

Tasks API:

`http://127.0.0.1:8000/api/tasks/`

### 3. Frontend Setup – Next.js

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the application:

`http://localhost:3000/`

The Next.js frontend communicates with the Django REST API to retrieve and display the available tasks.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks/` | Retrieve all available tasks |
| GET | `/api/tasks/1/` | Retrieve calculator task details |
| GET | `/api/tasks/2/` | Retrieve registration task details |

## Running Automated Tests

The project uses Pytest to validate task requirements.

Install Pytest if required:

```bash
pip install pytest
```

### Task 1 – Calculator

From the project root:

```bash
python -m pytest tasks/task-1-calculator/grader/ -v
```

### Task 2 – User Registration

```bash
python -m pytest tasks/task-2-registration/grader/ -v
```

The original starter implementations intentionally contain bugs. The graders are designed to detect incorrect behaviour.

Reference solutions should be tested separately to verify that all requirements are satisfied.

## Running Docker Containers

Make sure Docker Desktop is running before executing these commands.

Run all commands from the project root.

### Task 1 – Calculator

Build the Docker image:

```bash
docker build -t calculator-task ./tasks/task-1-calculator
```

Run the container:

```bash
docker run --rm calculator-task
```

### Task 2 – User Registration

Build the Docker image:

```bash
docker build -t registration-task ./tasks/task-2-registration
```

Run the container:

```bash
docker run --rm registration-task
```

## Application Features

- Displays available coding tasks.
- Shows task categories and difficulty levels.
- Displays task descriptions and requirements.
- Provides a detailed task view.
- Shows the execution environment for each task.
- Fetches task information from the Django REST API.
- Responsive user interface built with Next.js.

## Testing and Validation

The project includes automated test graders for both coding tasks.

Validation covers:
- Normal input scenarios.
- Edge cases.
- Invalid inputs.
- Expected error handling.
- Docker-based test execution.

The intentionally incorrect starter implementations demonstrate whether the graders can identify incorrect solutions.

## AI Tools Used

ChatGPT was used as an assistance tool during development for:

- Project planning and architecture.
- Understanding Docker configuration.
- Structuring coding tasks and automated graders.
- Debugging and implementation guidance.
- Documentation and README preparation.


## Author

**Teesha Vaza**

Full-Stack Developer

GitHub: [teesha1010](https://github.com/teesha1010)