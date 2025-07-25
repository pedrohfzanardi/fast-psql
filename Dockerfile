FROM python:3.12-slim-bookworm

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
ENV PYTHONPATH=/app/src
RUN uv venv && uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]