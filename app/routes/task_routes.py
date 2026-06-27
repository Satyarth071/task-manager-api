from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    response_description="The task has been successfully created."
)
def create_task(task_data: TaskCreate):
    """
    Create a new task with the following details:
    - **title**: Name of the task
    - **description**: Task details
    - **status**: Status of the task (Pending, In Progress, Completed)
    """
    return TaskService.create_task(task_data)


@router.get(
    "",
    response_model=List[TaskResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all tasks",
    response_description="A list of all tasks."
)
def get_tasks():
    """
    Retrieve the complete list of tasks stored in-memory.
    """
    return TaskService.get_all_tasks()


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
    summary="Update an existing task",
    response_description="The updated task details."
)
def update_task(task_id: str, task_data: TaskUpdate):
    """
    Update the title, description, or status of an existing task:
    - **task_id**: The UUID of the task to update
    - Request body fields are optional; only provided fields will be updated.
    
    Raises 404 if the task is not found.
    """
    updated_task = TaskService.update_task(task_id, task_data)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID '{task_id}' not found."
        )
    return updated_task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a task by ID",
    response_description="Confirmation message that the task was deleted."
)
def delete_task(task_id: str):
    """
    Delete a task by its unique ID.
    
    Raises 404 if the task is not found.
    """
    success = TaskService.delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID '{task_id}' not found."
        )
    return {"message": f"Task with ID '{task_id}' deleted successfully."}
