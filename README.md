# Orbital Witness Technical Task

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
5. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the React app:
   ```bash
   npm start
   ```

## Test

### Backend

1. Navigate to the `backend` directory.
2. Activate the virtualenvironment.
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
