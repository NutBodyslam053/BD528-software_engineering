# BD528-software_engineering

## Workflow

### 0. Create Github repository & Clone to local repository
```bash
git clone <github_repository_url>
```

### 1. Create template structure & Run to create needed directories
```bash
touch template.py
python template.py
```

### 2. Create virtual environment & Install dependencies
```bash
conda create -p venv python=3.9 -y
conda activate venv/
pip install -r requirements.txt
```

### 3. Initialize logger using constructor
```bash
src/mlProject/__init__.py
```

### 4. Create source code
    4.1 Update config.yaml
    4.2 Update schema.yaml
    4.3 Update params.yaml
    4.4 Update the entity
    4.5 Update the config
    4.6 Update the components
    4.7 Update the pipeline
    4.8 Update the main.py
    4.9 Update the app.py
