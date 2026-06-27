import uuid
from typing import List, Optional
from app.data import tasks_db
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate

class TaskService:
    """
    Service class handling operations on tasks.
    Encapsulates all task-related business logic and in-memory list operations.
    """

    @staticmethod
    def get_all_tasks() -> List[Task]:
        """
        Retrieve all tasks currently stored in memory.
        """
        return tasks_db

    @staticmethod
    def get_task_by_id(task_id: str) -> Optional[Task]:
        """
        Retrieve a task by its unique ID. Returns None if task does not exist.
        """
        for task in tasks_db:
            if task.id == task_id:
                return task
        return None

    @staticmethod
    def create_task(task_data: TaskCreate) -> Task:
        """
        Create a new task, generate a unique ID, store it in memory, and return the task.
        """
        # Automatically generate a unique UUID
        new_id = str(uuid.uuid4())
        new_task = Task(
            id=new_id,
            title=task_data.title,
            description=task_data.description,
            status=task_data.status
        )
        tasks_db.append(new_task)
        return new_task

    @staticmethod
    def update_task(task_id: str, task_data: TaskUpdate) -> Optional[Task]:
        """
        Update the attributes of an existing task. Returns the updated task or None if not found.
        """
        task = TaskService.get_task_by_id(task_id)
        if not task:
            return None
        
        # Only update attributes that were provided in the request
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.status is not None:
            task.status = task_data.status
            
        return task

    @staticmethod
    def delete_task(task_id: str) -> bool:
        """
        Delete a task by its ID. Returns True if deleted, False if task does not exist.
        """
        task = TaskService.get_task_by_id(task_id)
        if not task:
            return False
        tasks_db.remove(task)
        return True
