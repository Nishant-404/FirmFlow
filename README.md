# FirmFlow

A FastAPI-based backend application for business management.

## Setup

### Prerequisites
- Python 3.12+
- Git

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd FirmFlow
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\bin\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy psycopg pydantic python-multipart
```

### Running the Application

1. Start the development server:
```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:
- API: http://127.0.0.1:8000
- Interactive API docs: http://127.0.0.1:8000/docs
- Alternative API docs: http://127.0.0.1:8000/redoc

## Project Structure

```
FirmFlow/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py          # FastAPI app with debug prints
│       └── database.py      # Database configuration
├── main.py                  # Main FastAPI application
├── MVP_SCOPE.md            # Project scope and requirements
├── venv/                   # Virtual environment (not in git)
├── .gitignore
└── README.md
```

## API Endpoints

- `GET /` - Health check endpoint

## Development

The application uses:
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server for running the application
- **SQLAlchemy** - SQL toolkit and ORM
- **Psycopg** - PostgreSQL adapter
- **Pydantic** - Data validation using Python type annotations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.