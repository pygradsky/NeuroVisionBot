import os
from dataclasses import dataclass

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclass
class Data:
    data_dir: str = os.path.join(PROJECT_DIR, "data")
    downloads_dir: str = os.path.join(data_dir, "downloads")
