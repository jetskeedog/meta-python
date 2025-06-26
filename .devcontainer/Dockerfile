FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies if needed
USER root
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Switch back to non-root user
USER vscode