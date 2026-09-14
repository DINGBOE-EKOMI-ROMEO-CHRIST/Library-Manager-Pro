# Library Manager Pro

Library Manager Pro is a Python/FastAPI project for managing a library system.

## Requirements

Before starting, make sure you have installed:

* Python 3.x
* Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DINGBOE-EKOMI-ROMEO-CHRIST/Library-Manager-Pro.git
cd Library-Manager-Pro
```

### 2. Create a virtual environment

Create a Python virtual environment inside the project:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows — PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows — Command Prompt

```cmd
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

After activation, you should see `(.venv)` at the beginning of your terminal.

### 4. Install the dependencies

Install all required Python packages from `requiement.txt`:

```bash
pip install -r requiement.txt
```

### 5. Run the application

Start the FastAPI application with:

```bash
uvicorn main:app --reload
```

The API should then be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Project Structure

```text
Library-Manager-Pro/
│
├── AuthModule/
│   ├── Dependencies/
│   ├── Router/
│   ├── Schema/
│   ├── Security/
│   └── Service/
│
├── BookModule/
│   ├── Dependencies/
│   ├── Model/
│   ├── Repository/
│   ├── Router/
│   ├── Schema/
│   └── Service/
│
├── BorrowModule/
│   ├── Dependencies/
│   ├── Model/
│   ├── Repository/
│   ├── Router/
│   ├── Schema/
│   └── Service/
│
├── UserModule/
│   ├── Dependencies/
│   ├── Model/
│   ├── Repository/
│   ├── Router/
│   ├── Schema/
│   └── Service/
│
├── database_environnement.py
├── global_dependencies.py
├── main.py
├── requiement.txt
└── .gitignore
```

## Virtual Environment

The `.venv` directory is intentionally excluded from Git.

Each developer should create their own virtual environment locally:

```bash
python -m venv .venv
```

and install the project dependencies using:

```bash
pip install -r requiement.txt
```

## Development

When working on the project, make sure the virtual environment is activated before installing packages or running the application.

To deactivate the virtual environment:

```bash
deactivate
```
