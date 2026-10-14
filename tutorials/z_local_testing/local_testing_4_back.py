import sys
import os

# Local Testing
current_dir = os.path.dirname(os.path.abspath(__file__))

# Wrapped in one more dirname()
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

sys.path.insert(0, project_root)
# --------------------------