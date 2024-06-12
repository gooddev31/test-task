## Project Structure

- **routes**: Contains the API route definitions.
- **controllers**: Contains the logic for handling requests and responses.
- **database**: Contains database connection setup and models.
- **schemas**: Contains Pydantic models (schemas) for data validation and serialization.

## Prerequisites

- Python 3.7+
- Virtual environment tool (optional but recommended)

## Environment Variables

This project requires environment variables to be set for database and Redis connection URLs. Create a `.env` file in the project root and add the following variables:

```env
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
```

Replace `your_database_url` and `your_redis_url` with your actual database and Redis connection strings.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gooddev31/test-task.git
    cd test-task
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root with the following content:
    ```env
    DATABASE_URL=your_database_url
    REDIS_URL=your_redis_url
    ```

## Running the Project

1. **Start the FastAPI server**:
    ```sh
    uvicorn main:app --reload
    ```

    The server will start at `http://127.0.0.1:8000`.

## Project Structure Details

- **main.py**: The entry point of the application. It initializes the FastAPI app and includes the route definitions.

- **routes/**: This folder contains the API route definitions. Each file in this folder typically corresponds to a specific part of your API (e.g., `user_routes.py` for user-related endpoints).

- **controllers/**: This folder contains the business logic for handling requests and responses. Each controller typically corresponds to a specific part of your API (e.g., `user_controller.py` for user-related logic).

- **database/**:
  - **connection.py**: Contains the setup for database connection.
  - **models.py**: Contains the SQLAlchemy models representing the database schema.
  
- **schemas/**: This folder contains Pydantic models used for request validation and response serialization (e.g., `user_schema.py`).

