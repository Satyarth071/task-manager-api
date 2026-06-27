class Task:
    """
    Domain model representing a Task in the application.
    This model represents the core internal representation of the Task entity.
    """
    def __init__(self, id: str, title: str, description: str, status: str):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
