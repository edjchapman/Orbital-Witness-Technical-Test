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
   
### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```

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

## Implementation Details

- The backend API aggregates data from two endpoints and calculates usage credits based on specific rules.
- The frontend displays this data in a sortable table and a bar chart.

## Decisions and Concessions

- Simplified sorting logic for brevity.
- Focused on core functionality due to time constraints.
- With more time available, the credit calculations could be split into smaller functions for each condition.
  - This would simplify unit testing as calculations could be tested in isolation.

## Ambiguity

- Whitespace characters, unclear whether to include them in some metric counts.
  - Decided to not include them in unique words and palindrome checks.