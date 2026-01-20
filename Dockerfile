# 1. Base image: Playwright + browsers + system dependencies
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

# 2. Working directory inside the container
WORKDIR /usr/workspace

# 3. Copy dependencies separately (important for CI cache)
COPY requirements.txt .

# 4. Installing Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project into the container
COPY . .

# 6. Default command (what the container does when it starts)
CMD ["pytest", "-sv", "--alluredir=allure-results"]
