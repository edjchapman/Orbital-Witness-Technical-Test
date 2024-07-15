FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose the API port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
