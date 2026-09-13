# SPF (Science Paper Filter)

A web application for searching and ranking scientific papers based on user-provided keywords.

The project is primarily being developed as a learning project for understanding:

* Frontend and backend architecture
* TypeScript
* Python and FastAPI
* REST APIs and HTTP
* External APIs
* Scientific paper search
* Data processing and ranking
* LLM integration
* Potential future RAG/semantic search technologies

**!IMPORTANT NOTE!** This project is heavily assisted by the current ChatGPT free model, to write code, design project structure and write documentation.

## Project Architecture

The project is separated into a TypeScript frontend and a Python backend.

```text
Browser
   │
   ▼
TypeScript Frontend
   │
   │ HTTP / JSON
   ▼
FastAPI Backend
   │
   ├── OpenAlex API
   │
   ├── Paper processing
   │
   └── Ranking
   │
   ▼
JSON Response
   │
   ▼
TypeScript Frontend
```

## Technologies

### Frontend

* TypeScript
* Vite
* HTML
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Requests

### Data

* OpenAlex API

### Development

* pytest
* Ruff
* npm
* Python virtual environment

## Project Structure

```text
SPF/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── models/
│   │   │   ├── paper.py
│   │   │   ├── search.py
│   │   │   └── llm.py
│   │   ├── services/
│   │   │   ├── openalex.py
│   │   │   ├── ranking.py
│   │   │   ├── search.py
│   │   │   └── llm.py
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── pytest.ini
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── styles/
│   │   ├── api.ts
│   │   ├── main.ts
│   │   └── types.ts
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── README.md
└── run.sh
```

## How It Works

1. The user enters search keywords in the frontend.
2. TypeScript sends the keywords to the Python backend using an HTTP request.
3. FastAPI receives the request.
4. The backend searches OpenAlex for scientific papers.
5. Python processes and ranks the returned papers.
6. The backend sends the results back as JSON.
7. TypeScript receives the results.
8. The frontend displays the papers in the browser.

## Running the Project

### Backend

Create and activate the Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the backend:

```bash
cd backend
uvicorn app.main:app --reload
```

The backend will run on:

```text
http://localhost:8000
```

### Frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will normally run on:

```text
http://localhost:5173
```

Open the frontend address in a web browser.

## API

### Search Papers

```text
POST /search
```

Example request:

```json
{
    "keywords": [
        "evolution",
        "nature"
    ]
}
```

The backend returns a list of matching papers.

## Current Features

* [x] TypeScript frontend
* [x] FastAPI backend
* [x] OpenAlex paper search
* [x] Paper data models
* [x] Basic paper ranking
* [x] Citation-based ranking
* [x] Recency-based ranking
* [x] Frontend paper cards
* [x] Paper links
* [x] Backend/frontend communication
* [x] Automated tests
* [ ] Improved semantic paper search
* [ ] Additional scientific paper sources
* [ ] Improved ranking algorithm
* [ ] LLM-assisted relevance evaluation
* [ ] RAG / semantic retrieval
* [ ] Improved frontend UI

## Future Ideas

Possible future improvements include:

* RAG-based paper analysis
* LLM-assisted paper ranking
* Searching additional scientific databases
* More advanced ranking algorithms
* Filtering by publication year
* Filtering by citation count
* Open-access filtering
* Paper summaries
* Asking questions about retrieved papers
* Improved frontend design

## Development

This project is currently being developed as a learning project.

The main goal is not only to build a working application, but also to understand how the individual technologies work and how they communicate with each other.

Particular areas of study include:

```text
TypeScript
     ↓
Frontend
     ↓
HTTP / REST API
     ↓
FastAPI
     ↓
Python
     ↓
External APIs
     ↓
Data processing
     ↓
Ranking
```

## License

MIT License

Copyright (c) 2026 SPF

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
