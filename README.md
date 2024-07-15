# Orbital Witness Technical Task

# Option 1: Docker

## Project Setup with Docker Compose

## Quick Start

This project uses Docker Compose for an easy setup and consistent development environments.
Follow the steps below to get started.

### Requirements

- Docker
- Docker Compose

### Getting Started

1. **Clone the repository**:

   ```sh
   git@github.com:edjchapman/OrbitalWitness.git
   ```

2. **Navigate to the project root directory**:

   ```sh
   cd OrbitalWitness
   ```

3. **Build and start the services**:

   ```sh
   docker-compose up --build
   ```

   This command will build and start both the frontend and backend services.

4. **Access the frontend**:

   Open your browser and navigate to:
   ```sh
   http://localhost:3000/
   ```

5. **Access the API documentation**:

   Open your browser and navigate to:
   ```sh
   http://127.0.0.1:8000/redoc
   ```
   or
   ```sh
   http://127.0.0.1:8000/docs
   ```

### Directory Structure

Below is an overview of the relevant files and their purpose:

- `docker-compose.yml`: Docker Compose configuration file.
- `frontend/Dockerfile`: Dockerfile for the React frontend.
- `backend/Dockerfile`: Dockerfile for the FastAPI backend.

### Frontend Development

The React frontend is located in the `frontend` directory. 
Any changes made to the project files will be automatically reflected in the running Docker container.

### Backend Development

The FastAPI backend is located in the `backend` directory. 
Any changes made to the project files will be automatically reflected in the running Docker container.

### Stopping the Services

To stop the running services, use:

```sh
docker-compose down
```

This will stop and remove the containers, networks and volumes defined in the `docker-compose.yml` file.

### Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)

---

# Option 2: Non-Docker


## Setup

### Backend

1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
   
---

## Run

### Backend
1. Navigate to the `backend` directory.
2. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Run the React app:
   ```bash
   npm start
   ```
3. Visit the frontend at:
   ```bash
   http://localhost:3000/
   ```

---

## Docs

### API Docs
1. Run the backend.
2. Visit the docs:
   ```bash
   http://127.0.0.1:8000/redoc
   ```

---

## Test

### Backend

1. Navigate to the `backend` directory.
2. Activate the virtual environment.
3. Run the tests:
   ```bash
   pytest
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Run the tests:
   ```bash
   npm test
   ```

---

## Notes

### Implementation Details

- The backend API aggregates data from two endpoints and calculates usage credits based on specific rules.
- The frontend displays this data in a sortable table and a bar chart.
- The frontend should be accessible at `http://localhost:3000/`

### Ambiguity

- Whitespace characters: It was unclear whether to include them in some metric counts.
  - Decided to not include them in unique words and palindrome checks.