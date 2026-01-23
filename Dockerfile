# 1. Base image: Playwright + browsers + system dependencies
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

# 2. Working directory inside the container
WORKDIR /usr/workspace

# 3. Copy dependencies separately
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Setup Playwright with Chromium only
RUN playwright install chromium \
 && playwright install-deps chromium

# 5. Copy the entire project into the container
COPY . .