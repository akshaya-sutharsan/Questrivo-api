# AI Exam Paper Generator - Backend API

Flask REST API for the AI Exam Paper Generator (Sri Lankan syllabus).

## Setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your values
python run.py
```

## Structure

- `app/models` - SQLAlchemy models
- `app/controllers` - request handling logic
- `app/routes` - Flask blueprints
- `app/services` - AI generation and business logic
- `app/prompts` - prompt templates used by AI services

## Auth

JWT based. Register/login via `/api/auth/register` and `/api/auth/login`, then send
`Authorization: Bearer <token>` on protected routes.
