# Job API

A RESTful API built with FastAPI for managing job-related operations with user authentication and authorization.

## Features

- 🔐 **User Authentication** - JWT-based authentication system
- 👥 **User Management** - Create and manage user accounts
- 🔒 **Password Security** - Bcrypt password hashing with SHA-256 pre-hashing
- 📊 **Database Migrations** - Alembic for database schema management
- 🎯 **Standardized Responses** - Consistent API response format
- ⚡ **FastAPI** - High-performance, modern Python web framework
- 🗄️ **PostgreSQL** - Robust relational database support
- 🏗️ **SQLAlchemy ORM** - Database abstraction layer

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Bcrypt with SHA-256
- **Validation**: Pydantic

## Project Structure

```
job_api/
├── src/
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # Database configuration
│   ├── alembic.ini             # Alembic configuration
│   ├── dependencies/
│   │   └── session.py          # Database session dependency
│   ├── models/
│   │   ├── db/
│   │   │   └── user.py         # User database model
│   │   └── schemas/
│   │       ├── user.py         # User Pydantic schemas
│   │       └── response_model.py # Standardized response schema
│   ├── repository/
│   │   ├── crud/
│   │   │   ├── base.py         # Base CRUD repository
│   │   │   └── user.py         # User CRUD operations
│   │   └── table.py            # SQLAlchemy base table
│   ├── routes/
│   │   ├── endpoints.py        # Main router aggregator
│   │   ├── authentication.py  # Authentication endpoints
│   │   └── user.py             # User endpoints
│   ├── utilities/
│   │   ├── exceptions.py       # Custom exception handlers
│   │   ├── hash_generator.py  # Password hashing utilities
│   │   └── jwt_generator.py   # JWT token generation
│   └── migrations/
│       └── versions/           # Alembic migration files
└── .gitignore
```

## Prerequisites

- Python 3.11+
- PostgreSQL 12+
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd job_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   If `requirements.txt` doesn't exist, install manually:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-dotenv passlib[bcrypt] python-jose[cryptography] pydantic
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=postgresql://postgres:password@localhost:5432/job_db
   DATABASE_NAME=job_db
   DATABASE_PASSWORD=password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ```

6. **Set up the database**
   
   Create a PostgreSQL database:
   ```sql
   CREATE DATABASE job_db;
   ```

7. **Run database migrations**
   ```bash
   cd src
   alembic upgrade head
   ```

## Running the Application

1. **Start the development server**
   ```bash
   cd src
   uvicorn main:app --reload
   ```

2. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive API Docs (Swagger): `http://localhost:8000/docs`
   - Alternative API Docs (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Authentication

#### Sign Up
- **POST** `/auth/signup`
- **Description**: Create a new user account
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword123"
  }
  ```
- **Response**: Returns user data and JWT access token

### Users

#### Get All Users
- **GET** `/user/all`
- **Description**: Retrieve all users
- **Response**: List of all users

## Response Format

All API responses follow a standardized format:

### Success Response
```json
{
  "status": "success",
  "message": "Operation completed successfully",
  "data": { ... },
  "error": null
}
```

### Error Response
```json
{
  "status": "error",
  "message": "An error occurred",
  "data": null,
  "error": {
    "message": "Error details",
    "code": "ERROR_CODE"
  }
}
```

## Database Migrations

### Create a new migration
```bash
cd src
alembic revision --autogenerate -m "description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback migrations
```bash
alembic downgrade -1
```

## Development

### Code Structure

- **Models**: SQLAlchemy database models in `models/db/`
- **Schemas**: Pydantic schemas for request/response validation in `models/schemas/`
- **Routes**: API endpoints organized by feature in `routes/`
- **Repository**: Database operations in `repository/crud/`
- **Utilities**: Helper functions and exception handlers in `utilities/`

### Adding New Features

1. Create database model in `models/db/`
2. Create Pydantic schemas in `models/schemas/`
3. Create CRUD repository in `repository/crud/`
4. Create route handlers in `routes/`
5. Register routes in `routes/endpoints.py`
6. Create and run migrations

## Security Features

- **Password Hashing**: Passwords are hashed using SHA-256 + Bcrypt to handle passwords longer than 72 bytes
- **JWT Authentication**: Secure token-based authentication
- **Input Validation**: Pydantic schemas for request validation
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection

## Testing

```bash
# Run tests (when test suite is added)
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


