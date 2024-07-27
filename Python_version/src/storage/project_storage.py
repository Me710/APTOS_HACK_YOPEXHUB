# src/storage/project_storage.py
from src.models.project import Project

class ProjectStorage:
    def __init__(self):
        self.projects = {}
        self.next_id = 1

    def create_project(self, name: str, description: str, price: int, owner: str) -> Project:
        project = Project(self.next_id, name, description, price, owner)
        self.projects[self.next_id] = project
        self.next_id += 1
        return project

    def get_project(self, project_id: int) -> Project:
        return self.projects.get(project_id)

    def list_projects(self):
        return list(self.projects.values())