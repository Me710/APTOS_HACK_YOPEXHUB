# src/models/project.py
from dataclasses import dataclass

@dataclass
class Project:
    id: int
    name: str
    description: str
    price: int
    owner: str