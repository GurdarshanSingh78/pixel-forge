import subprocess
import os

# 1. Run your database setup script before the server starts
subprocess.run(["python", "initial_setup.py"])

# 2. Import your FastAPI app so Hugging Face can serve it
from app.main import app