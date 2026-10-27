# Cryptids of the World

A Flask frontend for browsing and managing cryptid sightings, backed by a FastAPI service.

## Requirements
- [uv](https://docs.astral.sh/uv/getting-started/installation/) **or** Python 3.13+ with pip
- A running instance of the FastAPI backend


## Setup

1. Install dependencies:

**With uv:**

```bash
uv sync
```

**With pip:**

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install "dotenv>=0.9.9" "flask>=3.1.3" "flask-login>=0.6.3" "flask-sqlalchemy>=3.1.1" "requests>=2.34.2"
```

2. Create a `.env` file in the project root with these variables:

```bash
FLASK_SECRET_KEY=your-secret-key-here
FLASK_DEBUG=1
FASTAPI_URL=http://localhost:8000
```

| Variable | Description |
|---|---|
| `FLASK_SECRET_KEY` | Signs session cookies and flash messages |
| `FLASK_DEBUG` | `1` enables debug mode and auto-reload; omit in production |
| `FASTAPI_URL` | Base URL of the FastAPI backend |

3. Generate a value for `FLASK_SECRET_KEY` with:

```bash
uv run flask shell               # pip users (venv active): flask shell
>>> import secrets
>>> secrets.token_hex(32)
```

### Running

**With uv:**

```bash
uv run flask run
```

**With pip** (venv active):

```bash
flask run
```
