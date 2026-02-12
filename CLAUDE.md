# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Support Engineer — an early-stage FastAPI backend that will serve as an AI-powered support assistant. The project uses Python 3.12, FastAPI, and Pydantic-settings for configuration.

## Repository Layout

- `backend/` — FastAPI application (the only active code area currently)
  - `app/main.py` — Application entry point, defines FastAPI app and routes
  - `app/config.py` — Pydantic-settings based configuration (`Settings` class, imported as `settings`)
  - `app/api/` — API route modules (scaffolded, not yet populated)
  - `app/services/` — Business logic services (scaffolded, not yet populated)
- `frontend/` — Frontend application (not yet started)

## Commands

### Running the backend locally
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Docker Compose (preferred)
```bash
docker compose up -d --build
docker compose down
```

### Setting up the Python environment
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**No test runner, linter, or formatter is configured yet.** If adding tests, use `pytest`. If adding linting, use `ruff`.

## Architecture Notes

- **FastAPI app** is created in `backend/app/main.py` and served via Uvicorn on port 8000.
- **Configuration** uses `pydantic_settings.BaseSettings` with `SettingsConfigDict` in `config.py`. Settings are case-sensitive, loaded from environment variables and `.env` file, and importable as `from app.config import settings`.
- **Secrets** — `OPENAI_API_KEY` is loaded from `.env` (gitignored) and passed to the backend container via `env_file` in `docker-compose.yml`. Never expose secrets in code or API responses.
- **Qdrant** — vector database running as a Docker Compose service, accessible at `http://qdrant:6333` from the backend container and `http://localhost:6333` from the host.
- **Request/response models** use Pydantic `BaseModel` (e.g., `ChatRequest`).
- Current endpoints: `GET /` (welcome), `GET /health` (health check), `GET /qdrant/health` (Qdrant health check), `GET /config` (project settings), `POST /chat` (echo-style chat placeholder).

## Conventions

- Commit messages are prefixed with `[MAJOR]` or `[MINOR]` to indicate scope of changes.
- Dependencies are managed via `backend/requirements.txt` (no pyproject.toml, no version pins).
- The Dockerfile uses `python:3.12-slim` as the base image.
- All Docker ports are bound to `127.0.0.1` (localhost only).
