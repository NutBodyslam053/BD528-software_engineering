# BD528-software_engineering

## Workflows

### 1. Create Github repository & Clone to local repository
```bash
git clone <github_repository_url>
```

### 2. Create template structure & Run to create needed directories
```bash
touch template.py
python template.py
```

### 3. Create virtual environment & Install dependencies
```bash
conda create -p venv python=3.9 -y
conda activate venv/
pip install -r requirements.txt
```

### 4. Initialize logger using constructor
```bash
src/mlProject/__init__.py
```

### 5. Create source code
    5.1 Update config.yaml
    5.2 Update schema.yaml
    5.3 Update params.yaml
    5.4 Update the entity
    5.5 Update the config
    5.6 Update the components
    5.7 Update the pipeline
    5.8 Update the main.py
    5.9 Update the app.py

## How to run?

### STEP 1: Clone the repository
```bash
git clone https://github.com/NutBodyslam053/winequality
```

### STEP 2: Create a conda environment & activate it
```bash
conda create -n <env_name> python=3.9 -y
conda activate <env_name>
```

### STEP 3: Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 4: Run application
```bash
python app.py
```

### STEP 5: Open the browser
> Diabetes Prediction Web-UI: http://localhost:8080

## For ML Developer
### Setup system environment variables

**For Unix-like shells (e.g., Bash, macOS Terminal):**
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/NutBodyslam053/BD528-software_engineering.mlflow
export MLFLOW_TRACKING_USERNAME=NutBodyslam053
export MLFLOW_TRACKING_PASSWORD=b85bafd69d98861fee89f5bf70dc5f62cf41c2e5
```

**For Windows PowerShell:**
```powershell
$env:MLFLOW_TRACKING_URI = "https://dagshub.com/NutBodyslam053/BD528-software_engineering.mlflow"
$env:MLFLOW_TRACKING_USERNAME = "NutBodyslam053"
$env:MLFLOW_TRACKING_PASSWORD = "b85bafd69d98861fee89f5bf70dc5f62cf41c2e5"
```

**For Windows Command Prompt:**
```bash
set MLFLOW_TRACKING_URI=https://dagshub.com/NutBodyslam053/BD528-software_engineering.mlflow
set MLFLOW_TRACKING_USERNAME=NutBodyslam053
set MLFLOW_TRACKING_PASSWORD=b85bafd69d98861fee89f5bf70dc5f62cf41c2e5
```

> MLflow tracking remote: https://dagshub.com/NutBodyslam053/mlflow-demo.mlflow