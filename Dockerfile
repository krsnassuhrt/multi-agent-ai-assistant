# =========================================
# Base Image
# =========================================
FROM python:3.11-slim

# =========================================
# Set Working Directory
# =========================================
WORKDIR /app

# =========================================
# Install System Dependencies (optional but safe)
# =========================================
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# =========================================
# Copy & Install Python Dependencies
# =========================================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# =========================================
# Copy Project Files
# =========================================
COPY . .

# =========================================
# Expose Port (Cloud Run expects 8080)
# =========================================
EXPOSE 8080

# =========================================
# Run FastAPI App
# =========================================
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]