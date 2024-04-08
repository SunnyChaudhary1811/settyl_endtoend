import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
API_DIR = os.path.join(PROJECT_ROOT, 'api')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
MODELS_DIR = os.path.join(PROJECT_ROOT, 'models')
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, 'notebooks')
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')
REQUIREMENTS_FILE = os.path.join(PROJECT_ROOT, 'requirements.txt')
README_FILE = os.path.join(PROJECT_ROOT, 'README.md')

if __name__ == "__main__":
    print("Project Structure:")
    print("Root Directory:", PROJECT_ROOT)
    print("API Directory:", API_DIR)
    print("Data Directory:", DATA_DIR)
    print("Models Directory:", MODELS_DIR)
    print("Notebooks Directory:", NOTEBOOKS_DIR)
    print("Source Directory:", SRC_DIR)
    print("Requirements File:", REQUIREMENTS_FILE)
    print("README File:", README_FILE)
