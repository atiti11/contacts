# Contacts API

A lightweight REST API for storing and managing personal contacts, built with **FastAPI** and backed by a **MySQL** database. The goal is to use this as a dummy API for learning REST API basis.

## Features

- **Add contacts** — store name, surname, phone, email, address, and notes
- **Look up contacts** — search by name & surname, or by ID
- **Delete contacts** — remove a contact by ID
- **Auth-protected** — all endpoints require a token passed via the `auth` header
- **Auto-docs** — interactive Swagger UI available at `/docs`

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Server | Hypercorn |
| Database | MySQL |
| Deployment | Railway / Vercel |

## Getting Started

### 1. Clone & install

```bash
git clone <your-repo-url>
cd contacts
pip install -r requirements.txt
```

### 2. Configure environment

Create a `.env` file in the project root:

```
AUTH_TOKEN=your_secret_token_here
```

> ⚠️ Never commit `.env` — it is already listed in `.gitignore`.

### 3. Run locally

```bash
hypercorn main:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive Swagger UI.

## API Endpoints

All requests require the header `auth: <your_token>`.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/contact?id=<id>` | Get contact by ID (or all contacts if no ID given) |
| `GET` | `/contact_2?name=<n>&surname=<s>` | Get contacts by name & surname |
| `POST` | `/contact` | Create a new contact |
| `DELETE` | `/contact` | Delete a contact by ID |

### POST `/contact` — form fields

| Field | Required | Description |
|---|---|---|
| `name` | ✅ | First name |
| `surname` | ✅ | Last name |
| `phone` | ❌ | Phone number |
| `email` | ❌ | Email address |
| `address` | ❌ | Physical address |
| `note` | ❌ | Free-text note |

## Deployment

The project includes configuration for both **Railway** (`railway.json`) and **Vercel** (`vercel.json`).

For Railway, set the `AUTH_TOKEN` environment variable in the Railway dashboard under your project's **Variables** tab.

## License

See [LICENSE.md](LICENSE.md).
