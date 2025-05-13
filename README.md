# React Networking Project

A web application built with React and Flask, featuring a modern UI and MongoDB integration.

## Project Structure

```
my-web-app/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   ├── constants/      # Application constants and configurations
│   │   ├── utils/         # Utility functions and helpers
│   │   ├── services/      # API service integrations
│   │   ├── pages/         # Page components
│   │   └── assets/        # Static assets (images, styles)
│   └── public/            # Public static files
└── backend/
|  ├── alembic/               # Alembic migrations
|  ├── configs/               # DB configs, environment configs
|  ├── models/                # SQLAlchemy models
|  ├── routes/                # FastAPI routers
|  ├── schemas/               # Pydantic schemas
|  ├── services/              # Business logic
|  ├── utils/                 # Auth, helpers
|  ├── test/                  # test folder 
|  ├── app.py                 # Entry point
|  ├── .env                   # Environment secrets
|  └── alembic.ini

Testing API and functions
test/
├── __init__.py
├── conftest.py                  # Shared fixtures (like DB session, client)
├── test_main.py                 # General app health check
├── routes/
│   ├── __init__.py
│   └── test_todo_routes.py      # Test `/todo` endpoints
├── services/
│   └── test_todo_service.py     # Optional: test services directly

```

## Features



## Setup

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

### Backend Setup

1. Create virtual environment:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start FastAPI(uvicorn) server:
   ```bash
   python app.py
   ```

## Dependencies

### Frontend
- React 19
- Bootstrap
- Font Awesome
- Highlight.js
- Fancybox

### Backend
- FastAPI
- MYSQL and PostgreSQL
- ALembic,Pydantic,Starlettte
- JWT Authorization and authentication
- pytest



## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request


## Author

Sanjog Harinkhede
