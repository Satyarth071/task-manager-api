from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="The title of the task")
    description: str = Field(..., description="Detailed description of the task")
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Current status of the task")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Build FastAPI backend",
                "description": "Create all routes, models, schemas, and services following clean architecture.",
                "status": "In Progress"
            }
        }
    }

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="New title of the task")
    description: Optional[str] = Field(None, description="New description of the task")
    status: Optional[TaskStatus] = Field(None, description="New status of the task")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Build FastAPI backend (Completed)",
                "description": "Completed all backend tasks and verified routes.",
                "status": "Completed"
            }
        }
    }

class TaskResponse(BaseModel):
    id: str = Field(..., description="Unique task identifier (automatically generated)")
    title: str = Field(..., description="Title of the task")
    description: str = Field(..., description="Description of the task")
    status: TaskStatus = Field(..., description="Current status of the task")

    # Config to allow reading attributes from standard python object (ORM mode in Pydantic v2)
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "e9bcf2b2-65f5-4122-83b5-77987df1c05d",
                "title": "Build FastAPI backend",
                "description": "Create all routes, models, schemas, and services following clean architecture.",
                "status": "In Progress"
            }
        }
    )
