FROM python:3.13

# Set working directory
WORKDIR /app

# Copy wheels and project
COPY wheels/ ./wheels/
COPY requirements.txt ./
COPY backend/ ./backend/

# Install dependencies from .whl files (offline)
RUN pip install --no-index --find-links=./wheels -r requirements.txt

# Start your backend app (replace with FastAPI/Flask if needed)
CMD ["python", "backend/main.py"]
