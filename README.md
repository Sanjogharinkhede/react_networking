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
    ├── app.py            # Flask application entry point
    ├── requirements.txt  # Python dependencies
    └── .env             # Environment variables
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

3. Start Flask server:
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
- Flask
- Flask-PyMongo
- Python-dotenv
- Flask-CORS



## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request


## Author

Sanjog Harinkhede
