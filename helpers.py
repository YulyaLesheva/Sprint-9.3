import random
import string
from pathlib import Path


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_email():
    return f'{generate_random_string(10)}@testmail.com'


def get_project_root():
    current_dir = Path(__file__).parent
    while True:
        if (current_dir / 'tests').exists():
            return current_dir
        current_dir = current_dir.parent


def get_resource_path(relative_path):
    project_root = get_project_root()
    return str(project_root / relative_path)
