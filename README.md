# Orbital Witness Technical Task

## Usage

Once the setup instructions have been completed below.

- [Frontend](http://127.0.0.1:3000/)
- [API Docs](http://127.0.0.1:8000/redoc)
- Frontend: Sort the table by credits used and/or report name by clicking the header name.

---

## Setup 

### Option 1: With Docker

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
   docker compose up --build
   ```

   This command will build and start both the frontend and backend services.

4. **Access the frontend**:

   Open your browser and navigate to:
   ```sh
   http://127.0.0.1:3000/
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
   
---

### Running the Tests

```sh
docker compose exec backend python -m pytest
```

---

### Stopping the Services

To stop the running services, use:

```sh
docker compose down
```

---

### Option 2: Non-Docker

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
   
---

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   # Node Version 18+
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
   http://127.0.0.1:3000/
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
   python -m pytest
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
- The frontend should be accessible at `http://127.0.0.1:3000/`

### Ambiguity

- Whitespace characters: It was unclear whether to include them in some metric counts.
  - Decided to not include them in unique words and palindrome checks.