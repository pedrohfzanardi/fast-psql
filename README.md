# fast-psql

This repository is an example backend application demonstrating how to build a modern Python API using [FastAPI](https://fastapi.tiangolo.com/) and PostgreSQL (PSQL), with a strong focus on reproducible development environments and best practices.

## Features

- **FastAPI** for high-performance, easy-to-use web APIs
- **PostgreSQL** as the database backend
- **Docker** for containerized development and deployment
- **Dev Containers** (`.devcontainer`) for a consistent VS Code development environment
- **uv** for fast and reliable Python dependency management
- **ruff** for linting and formatting Python code
- **pre-commit** hooks to enforce code quality automatically

## Getting Started

### Requirements

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) (recommended, with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers))

### Development Environment

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/fast-psql.git
   cd fast-psql
   ```

2. **Open in VS Code and Reopen in Dev Container:**
    Open the folder in VS Code.
    When prompted, "Reopen in Container" or use the Command Palette:
    Dev Containers: Reopen in Container

3. **The devcontainer will:**
    Build a Docker image with all dependencies
    Set up a Python virtual environment using uv
    Install all Python dependencies
    Enable pre-commit hooks and code linting/formatting


### Running the Application
   - With Docker Compose: `docker-compose up` </br>
     The API will be available at http://localhost:8000.

   - With Dev Container: </br>
      Use the integrated terminal to run:</br>
      `uvicorn src.main:app --reload --host 0.0.0.0 --port 8000`</br>
      You can also use the VS Code debugger: select "Python: FastAPI (main.py)" in the Run & Debug panel and start debugging.
    
## Code Quality 
 Ruff is used for linting and formatting.
 Run manually with: `pre-commit run --all-files`
 on commit to ensure code style and quality.
