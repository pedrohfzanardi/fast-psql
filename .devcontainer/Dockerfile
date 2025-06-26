FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies (optional, add as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add vscode user
RUN useradd -m vscode

# Set up workspace
WORKDIR /workspace

# Copy project files
COPY . /workspace

# Default shell
CMD ["/bin/bash"]