# Todo API

A simple API to manage tasks with CRUD operations

## Features
- **Create a Task**: Add a new task with title, description and due date.
- **Read Task**: Get a list of all tasks or specify task by ID.
- **Update a Task**: Modify task details, such as title or description.
- **Delete a Task**: Remove a task from the database

## Tech Stack
- Python
- FastAPI
- SQLModel

## Installation

1. Clone this repository:
  ```bash
  git clone https://github.com/Infamous003/todo-api.git
  cd todo-api
  ```

2. Install the required dependencies
  ```bash
  pip install -r requirements.txt
  ```

3. Run the app using uvicorn
  ```bash
  uvicorn app:app --reload
  ```

4. Enjoy :P
  Open http://127.0.0.1:8000/docs on your browser
